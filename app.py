from flask import Flask, render_template, request, redirect, url_for
import json
import os

# path to data folder
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# helper func for loading correct form data
def load_form(maltreatment_type_id):
    path = os.path.join(DATA_DIR, f'{maltreatment_type_id}.json')
    with open(path) as f:
        return json.load(f)

# dummy data for now
raters = ['', 'Alice', 'Bob', 'Cindy', 'David']
sites = ['', 'Bliss', 'Drum', 'JBLM']
maltreatment_types = ['', 'Child Physical', 'Child Sexual', 'Child Emotional', 'Child Neglect', 'Partner Physical', 'Partner Sexual', 'Partner Emotional', 'Partner Neglect']
maltreatment_type_ids = ['', 'child-physical', 'child-sexual', 'child-emotional', 'child-neglect', 'partner-physical', 'partner-sexual', 'partner-emotional', 'partner-neglect']

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic_info():
    return render_template('basic_info.html', raters=raters, sites=sites)

@app.route('/maltreatment-category')
def maltreatment_category():
    return render_template('maltreatement_category.html', maltreatment_types=maltreatment_types, maltreatment_type_ids=maltreatment_type_ids)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


@app.route('/medical-form')
def medical_form():
    maltreatment_type_id = request.args.get('type')  # or pull from session
    form_data = load_form(maltreatment_type_id)
    return render_template('medical_form.html', form=form_data)

@app.route('/housekeeping')
def housekeeping():
    return render_template('housekeeping.html')

if __name__ == '__main__':
    app.run(debug=True)