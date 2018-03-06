# render template that has to be imported
from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

# Articles = Articles()


@app.route('/')
def index():
    return render_template('home.html')        # pass your:render template


@app.route('/about')
def about():
    return render_template('about.html')        # pass your about template


@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)      # temp just id


if __name__ == '__main__':
    app.run(debug=True)
