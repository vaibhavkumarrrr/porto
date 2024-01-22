from flask import Flask, render_template

main = Flask(__name__)
EXP = [{
    "company": "Career Mantra",
    "postion": "Social media marketing intern",
    "location": "Remote",
    "duration": 3
}, {
    "company": "Nex gen media",
    "postion": "SMM",
    "location": "Remote",
    "duration": 1
}, {
    "company": "Nic",
    "postion": "Creative marketing lead",
    "location": "Bengaluru",
    "duration ": 26
}]


@main.route('/')
def index():
  return render_template("home.html", expr=EXP, fname="vk")


main.run(host='0.0.0.0', port=81, debug=True)
