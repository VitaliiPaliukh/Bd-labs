from flask import Flask, jsonify,g
from flasgger import Swagger
from flask_mysqldb import MySQL
from auth.dao.user_dao import UserDAO
from auth.controller.user_controller import user_bp
from auth.controller.flight_controller import flight_bp
from auth.controller.connected_flights_controller import connected_flights_bp
from auth.controller.ticket_controller import tickets_bp

app = Flask(__name__)
Swagger(app)

app.config['MYSQL_HOST'] = 'vitaliisql.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'VitaliPaliukh'
app.config['MYSQL_PASSWORD'] = 'Vitalik6837'
app.config['MYSQL_DB'] = 'airlinedb'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)


@app.before_request
def before_request():
    g.mysql = mysql

@app.route('/test-db')
def test_db():
    cur = g.mysql.connection.cursor()
    cur.execute("SHOW TABLES;")
    tables = cur.fetchall()
    cur.close()
    return jsonify({'tables': tables})

@app.route('/')
def home():
    return "Welcome to the Airline Database API!"

app.register_blueprint(connected_flights_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(flight_bp, url_prefix='/api')
app.register_blueprint(tickets_bp, url_prefix='/api/tickets')



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)






