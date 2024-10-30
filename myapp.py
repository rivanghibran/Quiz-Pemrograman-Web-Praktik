from flask import Flask, render_template
from config.db_config import init_db

app = Flask(__name__)
app.secret_key = 'pw'
mysql = init_db(app)

@app.route('/')
def home():
    return render_template('homepage.html', title='Home Page', name='World' )

@app.route('/about')
def about():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students") 
        data = cur.fetchall()
        cur.close()
        return render_template('about.html', title='About Us', students=data ) 
    except Exception as e:
        return f"An error occurred: {e}"
    


if __name__ == '__main__':
    app.run(debug=True)

