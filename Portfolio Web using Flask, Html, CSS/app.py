from flask import Flask, render_template, request
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print("New contact form submission:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    return f"<h2>Thanks {name}, your message has been received!</h2>"

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True)
