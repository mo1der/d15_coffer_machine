from flask import Flask
from flask import render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template('index.html', zmienna=random.randint(1, 10), page_year=datetime.date.today().year)

@app.route('/bye/<name>')
def say_bye(name):
    endpoint = "https://api.agify.io/"
    user_params = {"name": name}
    response = (requests.get(url=endpoint, params=user_params)).json()
    age = int(response["age"])

    endpoint2 = "https://api.genderize.io/"
    user_params2 = {"name": name}
    response2 = (requests.get(url=endpoint2, params=user_params2)).json()
    gender = response2["gender"]


    return f'<h1>Hey {name.title()},</h1>' \
           f'<h2>I think you are {gender},' \
           f'<h3>And maybe {age} years old.'


@app.route('/quess')
def quess():
    return "Bye"

@app.route('/blog')
def get_blog():
    endpoint3 = "https://api.npoint.io/c790b4d5cab58020d391"
    response3 = requests.get(url=endpoint3)
    all_posts = response3.json()
    return render_template('blog.html', posts=all_posts)

#
# @app.route('/blog/<num>')
# def get_blog(num):
#     endpoint3 = "https://api.npoint.io/c790b4d5cab58020d391"
#     response3 = requests.get(url=endpoint3)
#     all_posts = response3.json()
#     print(num)
#     return render_template('blog.html', aidi=int(num), posts=all_posts)
#
#


if __name__ == '__main__':
    app.run(debug=True, port=80)

