import webbrowser
from flask import Flask, render_template
from PIL import Image, ImageDraw
import math

app = Flask(__name__)

@app.route('/')
def index():
    # Load the image
    image_path = "static/WorldMap_Terra.png"
    image = Image.open(image_path)

    # Rotate the image by -45 degrees
    rotated_image = image.rotate(-45, expand=True)
    
    # Get the dimensions of the rotated image
    rotated_image_width, rotated_image_height = rotated_image.size
    
    # Save the rotated image temporarily
    rotated_image_path = "static/" + (image_path.split("/")[-1]).split(".")[0] + "_rotated.png"
    rotated_image.save(rotated_image_path)
    
    return render_template('index.html', image_path=rotated_image_path, image_width=rotated_image_width, image_height=rotated_image_height)

if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True, use_reloader=False)
