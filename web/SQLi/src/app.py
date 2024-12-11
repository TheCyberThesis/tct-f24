from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

# Home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = text(f"SELECT * FROM user WHERE username='{username}' AND password='{password}'")
        
        print(query)  # for debugging
        result = db.session.execute(query)

        user = result.fetchone()
        if user:
            # Store username in session
            session['username'] = user[1]  # Assuming user[1] is the username
            return redirect(url_for('flag'))  # Redirecting to /flag route without user in arguments
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

# Flag route
# Flag route
# Flag route
@app.route('/flag')
def flag():
    # Check if the user is logged in
    username = session.get('username')  # Get the username from the session
    if username == 'admin':
        # Read the flag from the file
        with open('flag.txt', 'r') as flag_file:
            flag = flag_file.read().strip()  # Read and strip any surrounding whitespace
        return render_template('flag.html', flag=flag, username=username)  # Pass the flag and username to the template
    else:
        return render_template('flag.html', flag=None, username=username)  # Pass None if not admin



# Database and admin creation function
def setup_database():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        admin_user = User(username='admin', password='adminP@551S_S3cuR3')
        db.session.add(admin_user)
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        setup_database()
    app.run(debug=True)

# if __name__ == '__main__':
#     with app.app_context():
#         setup_database()
#     app.run(host='0.0.0.0', port=5000, debug=True)  # Added host='0.0.0.0'

