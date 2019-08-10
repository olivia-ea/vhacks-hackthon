"""Models and databases"""

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    mentor = db.Column(db.Boolean())
    mentee = db.Column(db.Boolean())
    location = db.Column(db.String(50), nullable=True)
    industry = db.Column(db.String(50), nullable=True)
    skillset = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<User user_id={self.user_id}>'


# if __name__ == '__main__':
#     from server import app

#     connect_to_db(app)
#     db.create_all()
#     print('Connected to DB.')