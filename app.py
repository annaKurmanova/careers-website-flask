from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'San Fransisco',
        'salary': 'USD 100 000'
    },
{
        'id': 2,
        'title': 'Web developer',
        'location': 'Seattle',
        'salary': 'USD 130 000'
    },
{
        'id': 3,
        'title': 'Backend engineer',
        'location': 'New York',
        'salary': 'USD 250 000'
    }
]

@app.route("/")
def main_page():
    return render_template('home.html', jobs = JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)