from flask import Flask, render_template

main = Flask(__name__)
EXP = [{
    "company": "Career IN Mantra",
    "postion": "Social media marketing intern",
    "location": "Remote",
    "duration": 3}, 
    {"company": "Nex gen media",
    "postion": "SMM",
    "location": "Remote",
    "duration": },
    {"company":"mvj college of enginnering",
    "position": "student",
    "location": "bengaluru",
    "duration":24      }]


@main.route('/')
def index():
  return render_template('home.html', expr=EXP, fname="ANJALI")

if __name__ == "__main__":
  main.run(host='0.0.0.0', port=81, debug=True)
