import psycopg2

conn = psycopg2.connect(database="gora_db", host="postgres", user="postgres", password="root", port="5432")
cur = conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS  persons (id serial PRIMARY KEY, name varchar(100), age integer, sport varchar(100));''')
cur.execute('''INSERT INTO persons(name, age, sport) VALUES ('nazar', 23, 'football'), ('ostap', 23, 'basketball');''')


conn.commit()
cur.close()
conn.close() # use to close connection
