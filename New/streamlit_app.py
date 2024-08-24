import streamlit as st
import subprocess
import threading
import time
import requests

# Path to the Flask server script
FLASK_SERVER_PATH = r'C:\Users\ElphusK\Documents\GitHub\testing\New\flask_server.py'

# Function to run Flask server
def run_flask():
    subprocess.run(['python', FLASK_SERVER_PATH])

# Function to start Flask server in a separate thread
def start_flask():
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    time.sleep(10)  # Give Flask some time to start

def main():
    st.title("Flask Integrated with Streamlit")

    # Start Flask server
    start_flask()

    # Fetch and display content from Flask
    try:
        response = requests.get('http://127.0.0.1:8000/')
        if response.ok:
            st.write("Flask server is running and serving content.")
            st.components.v1.html(response.text, height=600, width=800)
        else:
            st.write(f"Failed to connect to Flask server. Status code: {response.status_code}")
    except requests.ConnectionError as e:
        st.write(f"Error connecting to Flask server: {e}")

if __name__ == '__main__':
    main()
