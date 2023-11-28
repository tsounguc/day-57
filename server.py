from datetime import datetime
import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home(name=None):
    random_number = random.randint(1, 10)
    copyright_year = datetime.now().year
    return render_template("index.html", name=name, num=random_number, copyright_year=copyright_year)

if __name__ == "__main__":
    app.run(debug=True)


