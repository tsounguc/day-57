from datetime import datetime
import random
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home(name=None):
    random_number = random.randint(1, 10)
    copyright_year = datetime.now().year

    return render_template("index.html", name=name, num=random_number, copyright_year=copyright_year)

@app.route('/guess/<string:name>')
def gues_page(name):
    name = name.title()
    agify_endpoint = f"https://api.agify.io?name={name}"
    genderize_endpoint = f"https://api.genderize.io?name={name}"

    agify_response = requests.get(url=agify_endpoint)
    agify_response.raise_for_status()
    agify_data = agify_response.json()

    genderize_response = requests.get(url=genderize_endpoint)
    genderize_response.raise_for_status()
    genderize_data = genderize_response.json()
    return render_template("index.html", name=name, gender=genderize_data['gender'], age=agify_data['age'])


@app.route('/blog/<int:num>')
def blog_page(num):
    blog_url = "https://api.npoint.io/31f3edd52b60ab8cee6e"
    blog_response = requests.get(url=blog_url)
    blog_response.raise_for_status()
    blog_data = blog_response.json()
    return render_template("blog.html", blogs=blog_data, num=num)


if __name__ == "__main__":
    app.run(debug=True)


