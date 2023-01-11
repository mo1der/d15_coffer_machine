from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=endpoint)
    all_posts = response.json()
    return render_template('index.html', posts=all_posts)

@app.route('/post/<num>')
def show_post(num):
    endpoint3 = "https://api.npoint.io/c790b4d5cab58020d391"
    response3 = requests.get(url=endpoint3)
    all_posts = response3.json()
    post = all_posts[int(num)-1]
    return render_template('post.html', post_title=post["title"], post_content=post["body"])

# @app.route('/blog/<num>')
# def get_blog(num):
#     endpoint3 = "https://api.npoint.io/c790b4d5cab58020d391"
#     response3 = requests.get(url=endpoint3)
#     all_posts = response3.json()
#     return render_template('blog.html', aidi=int(num), posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True, port=80)
