from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify,make_response
import psycopg2


app = Flask(__name__)


class PerformCRUD(object):

    def __init__(self):
        self.conn = psycopg2.connect("host='192.168.43.108' dbname=spandana_db user='spandana' password='spandanaabc'")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def create(self):
        input_data = [(1, 'spandana', 'spandana@gmail.com', '7386451813'), \
                      (2, "hari", "hari@gmail.com", "7386551813"), \
                      (3, "ram", "ram@gmail.com", "7386651813"), \
                      (4, "prem", "prem@gmail.com", "7386751813"), \
                      (5, "sai", "sai@gmail.com", "7386481813"), \
                      (6, "sp", "sp@gmail.com", "7386951813")]
        try:
            query = """INSERT INTO employees VALUES (%s, %s, %s, %s);"""
            [self.cursor.execute(query, data) for data in input_data]
            return make_response(jsonify({'status': 1}))
        except Exception as e:
            return make_response(jsonify({'status': str(e)}))
        finally:
            self.conn.commit()




    def update(self):
        try:

            query = """update employees set empname='harikris' where empid=2;
                    """

            self.cursor.execute(query)
            return make_response(jsonify({'status': 1}))

        except Exception as e:
            return make_response(jsonify({'status': str(e)}))
        finally:
            self.conn.commit()



    def delete(self):
        try:

            query = """DELETE FROM employees;"""
            self.cursor.execute(query)
            return make_response(jsonify({'status': 1}))
        except Exception as e:
            return make_response(jsonify({'status': str(e)}))
        finally:
            self.conn.commit()


    def read(self):
        try:

            query = """SELECT * FROM employees;"""
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                print(row)

            return make_response(jsonify({'status': 1}))
        except Exception as e:
            return make_response(jsonify({'status': str(e)}))
        finally:
            self.conn.commit()


@app.route('/', methods=['GET', 'POST'])
def home():
    obj = PerformCRUD()

    while True:
        i = input("Select Create\\Read\\Update\\Delete : ")
        if i == 'create':
            status = create(obj)
        if i == 'read':
            status = read(obj)
        if i == 'update':
            status = update(obj)
        if i == 'delete':
            status = delete(obj)
        co = input('Do you want to continue(y/n)?')
        if co == 'y':
            continue
        else:
            return status


@app.route('/create', methods=['POST'])
def create(obj):
    return obj.create()


@app.route('/read', methods=['GET'])
def read(obj):
    return obj.read()


@app.route('/update', methods=['PUT'])
def update(obj):
    return obj.update()


@app.route('/delete', methods=['DELETE'])
def delete(obj):
    return obj.delete()


if __name__ == "__main__":
    app.run(debug=True)