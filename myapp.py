from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'pw'

@app.route('/')
def home():
    return render_template('homepage.html', title='Home Page', name='World' )

@app.route('/about')
def register():
    return render_template('about.html', title='About Us' )


if __name__ == '__main__':
    app.run(debug=True)

