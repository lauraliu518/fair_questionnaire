from flask import Flask, render_template, request, redirect, url_for

# dummy data for now
raters = ['', 'Alice', 'Bob', 'Cindy', 'David']
sites = ['', 'Bliss', 'Drum', 'JBLM']

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic_info():
    return render_template('basic_info.html', raters=raters, sites=sites)

@app.route('/maltreatment-category')
def maltreatment_category():
    return render_template('maltreatement_category.html')



if __name__ == '__main__':
    app.run(debug=True)