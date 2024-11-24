from flask import Flask, jsonify,g
from flask_mysqldb import MySQL
from auth.dao.user_dao import UserDAO
from auth.controller.user_controller import user_bp
from auth.controller.flight_controller import flight_bp
from auth.controller.ticket_controller import tickets_bp
from auth.controller.connected_flights_controller import connected_flights_bp
from auth.controller.ticket_controller import tickets_bp

app = Flask(__name__)

# Налаштування бази даних
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Замініть на ваше ім'я користувача
app.config['MYSQL_PASSWORD'] = 'vitalik16'  # Замініть на ваш пароль
app.config['MYSQL_DB'] = 'airlinedb'  # Замініть на вашу базу даних
app.config['MYSQL_PORT'] = 3306  # Замініть на ваш порт

mysql = MySQL(app)


@app.before_request
def before_request():
    g.mysql = mysql

@app.route('/')
def home():
    return "Welcome to the Airline Database API!"

app.register_blueprint(connected_flights_bp, url_prefix='/api')
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(flight_bp, url_prefix='/api')
app.register_blueprint(tickets_bp, url_prefix='/api/tickets')



if __name__ == '__main__':
    app.run(debug=True, port=5000)






