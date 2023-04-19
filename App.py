from flask import Flask, render_template, request
import sqlite3 as lite

app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def hello():
    if request.method == 'POST':
        task = request.form.get('task')
        email = request.form.get('email')
        try:
            connection = lite.connect('task.sqlite')
            with connection:
                cursor = connection.cursor()
                sql = "insert into dev_takes_task values ('{}','{}')".format(task,email)
                cursor.execute(sql)
                cursor.execute('COMMIT;')
        except lite.Error as er:
            print(er)
            return 'an error occured... maybe duplicate entry ... choose another task'
        return 'thank you for submission'
    else:    
        return render_template('workshop.html')

@app.route('/create')
def create():
    with open('task.sqlite.sql') as f:
        sql = f.read()
        try:
            connection = lite.connect('task.sqlite')
            with connection:
                cursor = connection.cursor()
                for s in sql.split(';'):
                    cursor.execute(s)
        except lite.Error as er:
            print(er)
            return 'an error occured'
    return 'created table dev_takes_task'

@app.route('/admin')
def admin():
    out = ''
    try:
        connection = lite.connect('task.sqlite')
        with connection:
            cursor = connection.cursor()
            sql = "select * from dev_takes_task"
            cursor.execute(sql)
            myList = cursor.fetchall()
            for tup in myList:
                out += 'The Developer having email: ' + tup[1] + ' takes task: ' + tup[0] + '<br>'
    except lite.Error as er:
        print(er)
        return 'an error occured'
    return out

if __name__ == '__main__':
    app.run(debug=True)

