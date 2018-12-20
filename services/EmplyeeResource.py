from flask_restful import Resource
from model.Employe import Employee


class EmployeeResource(Resource):
    def get(self):
        # conn = db_connect.connect() # connect to database
        # query = conn.execute("select * from employees") # This line performs query and returns json result
        # return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
        employees = [Employee("Alan").__str__(), Employee("Rogelio").__str__()]
        return employees, 200
