# Urine_strip_color_detector
A Web Interface that allows users to upload an image of their urine strip and identify the colors on the strip.

## Requirements

- Python 3.8+
- Django==4.2.5
- numpy==1.26.0
- opencv-python==4.8.0.76
- Pillow==10.0.1
- scikit-learn==1.3.0

## Installation

1. Clone the repository: git clone https://github.com/Omkie-111/AlgoBulls-Todo.git

2. Change into the project directory: 

  ```
  cd urine_strip_app
  ```
  
3. Create a virtual environment: 

  ```
  python -m venv venv
  ```
  
4. Activate the virtual environment:

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

- On Windows:

  ```
  venv\Scripts\activate
  ```

5. Install the dependencies: 

  ```
  pip install -r requirements.txt
  ```
  
6. Apply the database migrations: 

  ```
  python manage.py migrate
  ```
  
7. Run the development server: 
 
  ```
  python manage.py runserver
  ```
  
The app will be accessible at `http://localhost:8000/`.

## Usage

- Access the web interface at `http://localhost:8000/` to check the urine color strip.
