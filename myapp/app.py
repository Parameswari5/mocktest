from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'database-1.c3o48ykik01d.ap-south-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Parameswari'
app.config['MYSQL_DB'] = 'studentdb'

mysql = MySQL(app)

# Home route to display all students
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', students=data)

# Route to add a new student
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO students (name, email) VALUES (%s, %s)", (name, email))
    mysql.connection.commit()
    cur.close()
    return redirect('/')

# Route to update an existing student
@app.route('/update/<id>', methods=['POST'])
def update(id):
    name = request.form['name']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE students SET name=%s, email=%s WHERE id=%s", (name, email, id))
    mysql.connection.commit()
    cur.close()
    return redirect('/')

# Route to delete a student
@app.route('/delete/<id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", [id])
    mysql.connection.commit()
    cur.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
