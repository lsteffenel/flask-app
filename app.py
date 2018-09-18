from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-32501-1365253458-0.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-22919-1365255114-2.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr03/2013/4/6/9/anigif_enhanced-buzz-24011-1365253511-0.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-32505-1365253605-4.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-32585-1365253559-0.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr03/2013/4/6/9/anigif_enhanced-buzz-23997-1365253763-3.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-22675-1365255333-0.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr01/2013/4/6/9/anigif_enhanced-buzz-578-1365255277-0.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/9/anigif_enhanced-buzz-22911-1365255823-0.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/enhanced/webdr06/2013/4/6/8/anigif_enhanced-buzz-22680-1365251927-5.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
