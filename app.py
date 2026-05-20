from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic_info():
    raters = ['Alice', 'Bob', 'Cindy', 'David']
    return render_template('basic_info.html', raters=raters)



if __name__ == '__main__':
    app.run(debug=True)