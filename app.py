from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Kapil Chaudhary',
        'title' : 'Recurrent Neural Network',
        'content' : 'How RNN Works?',
        'date_posted': 'March 8, 2025'
    },
    {
        'author': 'Kapil Chaudhary',
        'title' : 'Long-Short Term Memory',
        'content' : 'How LSTM Works?',
        'date_posted': 'March 8, 2025'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__ == "__main__":
    app.run(debug=True)
