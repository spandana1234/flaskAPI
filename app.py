from config import *

emp_schema = EmpSchema()
emps_schema = EmpSchema(many=True)


@app.route('/emps', methods=['POST'])
def create_emp():
    emp_name = request.json['emp_name']
    email = request.json['email']
    new_emp = Employee(emp_name, email)

    db.session.add(new_emp)
    db.session.commit()

    return emp_schema.jsonify(new_emp)


@app.route('/emps', methods=['GET'])
def get_emps():
    all_emps = Employee.query.all()
    result = emps_schema.dump(all_emps)
    return jsonify(result)


@app.route('/emps/<id>', methods=['GET'])
def get_emp(id):
    emp = Employee.query.get(id)
    return emp_schema.jsonify(emp)


@app.route('/emps/<id>', methods=['PUT'])
def update_emp(id):
    emp = Employee.query.get(id)
    emp_name = request.json['emp_name']
    email = request.json['email']
    emp.emp_name = emp_name
    emp.email = email
    db.session.commit()
    return emp_schema.jsonify(emp)


@app.route('/emps/<id>', methods=['DELETE'])
def delete_emp(id):
    emp = Employee.query.get(id)
    db.session.delete(emp)
    db.session.commit()
    return emp_schema.jsonify(emp)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 1})


if __name__ == "__main__":
    app.run(debug=True)
