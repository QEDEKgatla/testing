from flask import Flask, send_from_directory, request, redirect, url_for, render_template_string, session
import os
app = Flask(__name__, static_folder=r'New folder/static')

# Set a secure secret key for session management
app.secret_key = 'your_secret_key_here'  # Replace with your actual secret key

# HTML for the login page
login_page = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .login-container {
            text-align: center;
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 8px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            width: 400px;  /* Adjust the width as needed */
        }
        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        input[type="text"],
        input[type="password"] {
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            width: 100%;
        }
        input[type="submit"] {
            padding: 10px;
            border: none;
            border-radius: 4px;
            background-color: #007bff;
            color: #fff;
            cursor: pointer;
            width: 100%;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login Page</h2>
        <form method="POST" action="/login">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    </div>
</body>
</html>
'''

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check credentials
        if username == 'EliaOnMove' and password == '123456':
            session['logged_in'] = True  # Mark the user as logged in
            return redirect(url_for('index'))
        else:
            return "Invalid credentials! Please try again."
    return render_template_string(login_page)

# Route to serve the HTML file
@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return send_from_directory(r'New folder/static', 'T.html')

# Route to serve static files
@app.route('/copperlichtdata/<path:filename>')
def serve_static(filename):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return send_from_directory(r'New folder/static/copperlichtdata', filename)

# Route to log out
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
