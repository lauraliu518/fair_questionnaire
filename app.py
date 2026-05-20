from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Pass dynamic variables directly to the template
    return render_template('basic_info.html', title="Home Page", user="Developer")

if __name__ == '__main__':
    app.run(debug=True)