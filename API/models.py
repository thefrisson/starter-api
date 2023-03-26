from . import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(40), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    users = db.relationship('UsersProjects', backref='project', lazy=True)
    apps = db.relationship('DigitalOceanApp', backref='project', lazy=True)
    

    def __repr__(self):
        return '<Project %r>' % self.name

class UsersProjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'), nullable=False)

    def __repr__(self):
        return '<UsersProjects %r>' % self.id
    




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    manage_apps = db.Column(db.Boolean, nullable=False)

    projects = db.relationship('UsersProjects', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.email

    def check_password(self, password):
        return self.password == password


class DigitalOceanApp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
