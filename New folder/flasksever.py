from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=r'New Folder\New folder\static')

# Route to serve static files
@app.route('/copperlichtdata/<path:filename>')
def serve_static(filename):
    return send_from_directory(r'C:\Users\ElphusK\Videos\New Folder\New folder\static\copperlichtdata', filename)

# Route to serve the HTML file
@app.route('/')
def index():
    return send_from_directory(r'C:\Users\ElphusK\Videos\New Folder\New folder\static', 'T.html')

if __name__ == '__main__':
    app.run(port=8000)
