from flask import Flask, render_template, jsonify
import subprocess
import os

# Create the Flask app and specify the custom template folder location
app = Flask(__name__, template_folder=r'C:\Users\ElphusK\Videos\New Folder\New Folder (2)\New folder\New folder')

@app.route('/')
def index():
    return render_template('index.html')  # Renders index.html from the specified folder

@app.route('/run-game', methods=['POST'])
def run_game():
    try:
        # Run the executable file with the correct path
        exe_path = r'C:\Users\ElphusK\Videos\New Folder\New Folder (2)\New folder\New folder\myGame.exe'
        subprocess.run([exe_path], check=True)
        return jsonify({"status": "success", "message": "Game executed successfully."})
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
