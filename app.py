import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(database="gora_db", host="postgres", user="postgres", password="root", port="5432")
    
    # Ensure the table is created whenever a connection is made
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS persons (
                    id serial PRIMARY KEY, 
                    name varchar(100), 
                    age integer, 
                    sport varchar(100)
                );''')
    conn.commit()  # Make sure to commit the creation
    cur.close()
    
    return conn

@app.route('/')
def index():
    conn = db_conn()
    cur = conn.cursor()
    
    # Insert records only if table is empty
    cur.execute('''SELECT COUNT(*) FROM persons;''')
    count = cur.fetchone()[0]
    
    if count == 0:
        cur.execute('''INSERT INTO persons(name, age, sport) 
                       VALUES ('nazar', 23, 'football'), ('ostap', 23, 'basketball');''')
        conn.commit()

    cur.execute('''SELECT * FROM persons''')
    data = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return render_template('index.html', data=data)

@app.route('/delete', methods=['POST'])
def delete():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''DELETE FROM persons''')
    conn.commit()
    cur.close()
    conn.close()
    
    message = "All records deleted successfully"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

