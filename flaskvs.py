from flask import Flask, send_from_directory
import os
app = Flask(__name__, static_folder=r'New folder/static')

# Route to serve static files
@app.route('/copperlichtdata/<path:filename>')
def serve_static(filename):
    return send_from_directory(r'New folder/static/copperlichtdata', filename)

# Route to serve the HTML file
@app.route('/')
def index():
    return send_from_directory(r'New folder/static', 'T.html')

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
