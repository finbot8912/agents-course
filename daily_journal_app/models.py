from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    project = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    assignee = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Task {self.project} {self.date}>"

class StudyLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    reference = db.Column(db.String(200), nullable=True)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<StudyLog {self.title} {self.date}>"

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(200), nullable=False)

class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    content = db.Column(db.Text, nullable=False)
