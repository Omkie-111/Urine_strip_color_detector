from django.shortcuts import render, redirect, get_object_or_404
from .forms import UrineStripUploadForm
import cv2
import json
import numpy as np
from sklearn.cluster import KMeans
from .models import UrineStrip  

def analyze_urine_strip(request):
    if request.method == 'POST':
        form = UrineStripUploadForm(request.POST, request.FILES)
        if form.is_valid():
            urine_strip = form.save(commit=False)
            # Analyze the uploaded image using OpenCV to extract color information.
            # Store the results in the 'colors_json' field of the model.
            colors = analyze_image(urine_strip.image)
            urine_strip.colors_json = colors
            urine_strip.save()
            return redirect('result', pk=urine_strip.pk)
    else:
        form = UrineStripUploadForm()
    return render(request, 'upload.html', {'form': form})

def analyze_image(uploaded_image):
    # Read the uploaded image as a NumPy array
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)

    # Convert the image to the LAB color space for better color analysis
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Reshape the image to a 2D array of pixels
    pixels = lab_image.reshape((-1, 3))

    # Define the number of dominant colors to extract (e.g., 10)
    k = 10

    # Use scikit-learn's KMeans clustering to find the dominant colors
    kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)  # Changed 'n_init' to a fixed value
    kmeans.fit(pixels)

    # Get the RGB values of the dominant colors
    dominant_colors = [list(map(int, color)) for color in kmeans.cluster_centers_]

    # Create a JSON object with the dominant colors
    result = {"dominant_colors": dominant_colors}

    # Return the JSON result
    return json.dumps(result)

def result(request, pk):
    urine_strip = get_object_or_404(UrineStrip, pk=pk)
    result = json.loads(urine_strip.colors_json)
    
    dominant_colors = {
        'URO': result["dominant_colors"][0],
        'BIL': result["dominant_colors"][1],
        'KET': result["dominant_colors"][2],
        'BLD': result["dominant_colors"][3],
        'PRO': result["dominant_colors"][4],
        'NIT': result["dominant_colors"][5],
        'LEU': result["dominant_colors"][6],
        'GLU': result["dominant_colors"][7],
        'SG': result["dominant_colors"][8],
        'PH': result["dominant_colors"][9],
    }

    return render(request, 'result.html', {'urine_strip': dominant_colors})
