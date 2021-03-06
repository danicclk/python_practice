# # render template that has to be imported
# from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
# from data import Articles
# from flask_mysqldb import MySQL
# from wtforms import Form, StringField, TextAreaField, PasswordField, validators
# from passlib.hash import sha256_crypt
# from functools import wraps


# app = Flask(__name__)

# # Config MySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# # app.config['MYSQL_PASSWORD'] = '123456'
# app.config['MYSQL_DB'] = 'myflaskapp'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Display as a Dictionary
# # init MYSQL
# mysql = MySQL(app)  # wrapped up my app, use this to create cursors &queries

# # Articles = Articles()


# @app.route('/')
# def index():
#     # Create cursor
#     cur = mysql.connection.cursor()

#     # Get users
#     result = cur.execute("SELECT * FROM users")

#     users = cur.fetchall()
#     print(users)

#     if result > 0:
#         return render_template('home.html', users=users)

#     else:
#         msg = 'No Users Found'
#         return render_template('home.html', msg=msg)
#     # Close connection
#     cur.close()

# # About


# @app.route('/about')
# def about():
#     return render_template('about.html')        # pass your about template


# @app.route('/articles')
# def articles():
#     return render_template('articles.html', articles=Articles)


# @app.route('/article/<string:id>/')
# def article(id):
#     return render_template('article.html', id=id)      # temp just id


# class RegisterForm(Form):
#     name = StringField('Name', [validators.Length(min=1, max=50)])
#     username = StringField('Username', [validators.Length(min=4, max=25)])
#     email = StringField('Email', [validators.Length(min=6, max=50)])
#     password = PasswordField('Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Password do not match')
#     ])
#     confirm = PasswordField('Confirm Password')


# # User Register
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm(request.form)
#     if request.method == 'POST' and form.validate():
#         name = form.name.data
#         email = form.email.data
#         username = form.username.data
#         password = sha256_crypt.encrypt(str(form.password.data))  # encrypted

#         # Create cursor
#         cur = mysql.connection.cursor()

#         # Execute query
#         cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",  # string- replacements
#                     (name, email, username, password))  # variables assigned in request form above.

#         # Commit to DB
#         mysql.connection.commit()

#         # Close connection
#         cur.close()

#         flash('You are now registered and can log in', 'success')

#         return redirect(url_for('login'))
#     return render_template('register.html', form=form)


# # User login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         # Get Form Fields
#         username = request.form['username']
#         password_candidate = request.form['password']

#         # Create cursor
#         cur = mysql.connection.cursor()

#         #  Get user by username
#         result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

#         if result > 0:
#             # Get stored hash
#             data = cur.fetchone()  # It's only gonna fetch one, first w that username
#             password = data['password']

#             # Compare Passwords
#             if sha256_crypt.verify(password_candidate, password):
#                 app.logger.info('PASSWORD MATCHED')
#         else:
#             app.logger.inf('NO USER')

#     return render_template('login.html')


# if __name__ == '__main__':
#     app.secret_key = 'secret123'
#     app.run(debug=True)
