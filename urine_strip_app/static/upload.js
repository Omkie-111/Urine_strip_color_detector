$(document).ready(function() {
    $('#uploadForm').submit(function(e) {
        e.preventDefault();

        var formData = new FormData(this);

        $.ajax({
            url: '/urine_strip/process_image/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                if (data.colors) {
                    displayColors(data.colors);
                } else {
                    alert('No color data received.');
                }
            },
            error: function() {
                alert('Error processing the image.');
            }
        });
    });

    function displayColors(colors) {
        var resultDiv = $('#result');
        resultDiv.empty();
        for (var i = 0; i < colors.length; i++) {
            var colorBox = $('<div></div>');
            colorBox.css('background-color', 'rgb(' + colors[i][0] + ',' + colors[i][1] + ',' + colors[i][2] + ')');
            resultDiv.append(colorBox);
        }
    }
});
