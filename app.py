from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media2.giphy.com/media/eN2chYe9jwGw8/giphy.gif?cid=ecf05e47xneueabtv478wiipupx6g36obffm6ulg47vmw86b&rid=giphy.gif",
    "https://media0.giphy.com/media/Z8BXzZrix8pMI/giphy.gif?cid=ecf05e47f55e7895c0c0e79c9f27271977d321dc3bcc10b0&rid=giphy.gif",
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
