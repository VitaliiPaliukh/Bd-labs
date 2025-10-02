from auth.dto.user_dto import UserDTO
from flask import current_app
from flask import g


class UserDAO:
    @staticmethod
    def get_all_users():
        conn = g.mysql.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        cursor.close()

        # Construct a list of user dictionaries
        return [UserDTO(row[0], row[1], row[2]) for row in users]

    @staticmethod
    def create_user(username, email, password_hash):
            conn = g.mysql.connection
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)',
                (username, email, password_hash)
            )
            conn.commit()
            user_id = cursor.lastrowid
            cursor.close()

            return UserDTO(user_id, username, password_hash)
