# render template that has to be imported
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps


app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

# Articles = Articles()


@app.route('/')
def index():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get users
    result = cur.execute("SELECT * FROM users")

    users = cur.fetchall()
    print(users)

    if result > 0:
        return render_template('home.html', users=users)

    else:
        msg = 'No Users Found'
        return render_template('home.html', msg=msg)
    # Close connection
    cur.close()


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
