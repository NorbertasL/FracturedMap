from flask import Flask, render_template
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    # Load the image
    image_path = "static/WorldMap_Aerhen.png"
    image = Image.open(image_path)
    image_width, image_height = image.size
    
    return render_template('index.html', image_width=image_width, image_height=image_height)

if __name__ == '__main__':
    app.run(debug=True)