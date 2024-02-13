import psycopg2
from flask import Flask,render_template

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(database="gora_db",host="postgres",user="postgres",password="root",port="5432")
    return conn


@app.route('/')
def index():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS  persons (id serial PRIMARY KEY, name varchar(100), age integer, sport varchar(100));''')
    cur.execute('''INSERT INTO persons(name, age, sport) VALUES ('nazar', 23, 'football'), ('ostap', 23, 'basketball');''')
    cur.execute('''SELECT * FROM persons''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html',data=data)

@app.route('/delete', methods=['POST'])
def delete():
        conn = db_conn()
        cur = conn.cursor()
        cur.execute('''DELETE FROM persons''')
        conn.commit()
        conn.close()
        message = "All records deleted successfully"
        return render_template('index.html', message=message)
    
