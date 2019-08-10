"""Models and databases"""

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

class Seeking_Help_User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<eeking_Help_User user_id={self.user_id}>'

class Looking_To_Help_User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Looking_To_Help_User user_id={self.user_id}>'

# if __name__ == '__main__':
#     from server import app

#     connect_to_db(app)
#     db.create_all()
#     print('Connected to DB.')