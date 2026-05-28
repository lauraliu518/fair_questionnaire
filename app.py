from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
import sqlite3

# Paths
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
DATABASE = os.path.join(os.path.dirname(__file__), 'database', 'fair_questionnaire.db')

# Database functions 

# Connect to db
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  
    return conn

# Create submissions table if none exist
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            submitted_at TEXT    NOT NULL,
            data         TEXT    NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Verify db file, table, and row count
def check_db():
    print("\n--- DB check ---")
    # check if .db file exist
    if os.path.exists(DATABASE):
        print(f"[ok] database file found:  {DATABASE}")
    else:
        print(f"[!!] database file MISSING: {DATABASE}")
        return

    # check connection count
    try:
        conn = get_db_connection()
        row = conn.execute("SELECT COUNT(*) AS count FROM submissions").fetchone()
        print(f"[ok] connected successfully")
        print(f"[ok] submissions table exists — {row['count']} row(s) in db")
        conn.close()
    except Exception as e:
        print(f"[!!] connection or query failed: {e}")
    print("----------------\n")

# helper func for loading correct form data
# TODO: migrate to db retrieval
def load_form(maltreatment_type_id):
    path = os.path.join(DATA_DIR, f'{maltreatment_type_id}.json')
    with open(path) as f:
        return json.load(f)

# TODO: test data, remove later
raters = ['', 'Alice', 'Bob', 'Cindy', 'David']
sites  = ['', 'Bliss', 'Drum', 'JBLM']
maltreatment_types    = ['', 'Child Physical', 'Child Sexual', 'Child Emotional',
                         'Child Neglect', 'Partner Physical', 'Partner Sexual',
                         'Partner Emotional', 'Partner Neglect']
maltreatment_type_ids = ['', 'child-physical', 'child-sexual', 'child-emotional',
                         'child-neglect', 'partner-physical', 'partner-sexual',
                         'partner-emotional', 'partner-neglect']

app = Flask(__name__)
init_db()
check_db()

# flask routes
@app.route('/', methods=['GET', 'POST'])
def basic_info():
    return render_template('basic_info.html', raters=raters, sites=sites)

@app.route('/maltreatment-category')
def maltreatment_category():
    return render_template('maltreatement_category.html', maltreatment_types=maltreatment_types, maltreatment_type_ids=maltreatment_type_ids)

# route to confirmation page: POST saves submission data; GET jumps to confimation page
@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    if request.method == 'POST':
        payload = request.get_json()

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        sql = "INSERT INTO submissions (submitted_at, data) VALUES (?, ?)"
        cursor.execute(sql, (
            payload['submitted_at'],
            json.dumps(payload['data'])
        ))
        conn.commit()
        conn.close()

        return jsonify({'status': 'ok'})

    return render_template('confirmation.html')

@app.route('/medical-form')
def medical_form():
    maltreatment_type_id = request.args.get('type')  # or pull from session
    form_data = load_form(maltreatment_type_id)
    return render_template('medical_form.html', form=form_data)

@app.route('/housekeeping')
def housekeeping():
    return render_template('housekeeping.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM submissions').fetchall()
    conn.close()

    parsed = []
    for row in rows:
        data = json.loads(row['data'])
        parsed.append({
            'id': data["basic_info"]["case_number"],
            'date': data["basic_info"]["date"],
            'rater1': data["basic_info"]["rater1"],
            'rater2': data["basic_info"]["rater2"],
            'site': data["basic_info"]["site"]
        })

    return render_template('admin_dashboard.html', rows=parsed, raters=raters, sites=sites)

if __name__ == '__main__':
    app.run(debug=True, port=5001)