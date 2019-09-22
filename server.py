from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """Show homepage"""

    return render_template('index.html')


@app.route('/api/posts', methods=['GET'])
def show_post():
    """Show post form"""

    return render_template('make_post.html')


@app.route('/api/posts', methods=['POST'])
def process_post():
    """Process post form"""

    post = request.form['post']
    author = request.form['author']

    return render_template('posts.html', post=post, author=author)


if __name__ == "__main__":

    app.run(port=5000, host='0.0.0.0')



