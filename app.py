from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://i.giphy.com/media/eN2chYe9jwGw8/giphy.webp",
    "https://i.giphy.com/media/Z8BXzZrix8pMI/giphy.webp",
    "https://i.giphy.com/media/hXCGdsSC3MKuqZv59G/giphy.webp",
    "https://i.giphy.com/media/dxqOkrl29R8ac/giphy.webp",
    "https://i.giphy.com/media/5ESbl4pWvj2M0/giphy.webp"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
