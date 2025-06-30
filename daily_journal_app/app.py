from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, date
from models import db, Task, StudyLog, Meeting, Memo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    today = date.today()
    tasks = Task.query.filter_by(date=today).all()
    studies = StudyLog.query.filter_by(date=today).all()
    meetings = Meeting.query.filter(Meeting.date.like(f"{today}%")).all()
    memos = Memo.query.filter_by(date=today).all()
    return render_template('index.html', tasks=tasks, studies=studies, meetings=meetings, memos=memos, today=today)

@app.route('/add_task', methods=['POST'])
def add_task():
    t = Task(
        date=datetime.strptime(request.form['date'], '%Y-%m-%d').date(),
        project=request.form['project'],
        details=request.form['details'],
        start_date=datetime.strptime(request.form['start_date'], '%Y-%m-%d').date() if request.form['start_date'] else None,
        end_date=datetime.strptime(request.form['end_date'], '%Y-%m-%d').date() if request.form['end_date'] else None,
        assignee=request.form['assignee']
    )
    db.session.add(t)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_study', methods=['POST'])
def add_study():
    s = StudyLog(
        date=datetime.strptime(request.form['date'], '%Y-%m-%d').date(),
        title=request.form['title'],
        reference=request.form.get('reference'),
        content=request.form['content']
    )
    db.session.add(s)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_meeting', methods=['POST'])
def add_meeting():
    m = Meeting(
        date=datetime.strptime(request.form['datetime'], '%Y-%m-%dT%H:%M'),
        description=request.form['description']
    )
    db.session.add(m)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_memo', methods=['POST'])
def add_memo():
    memo = Memo(
        date=datetime.strptime(request.form['date'], '%Y-%m-%d').date(),
        content=request.form['content']
    )
    db.session.add(memo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    tasks = Task.query.order_by(Task.date.desc()).all()
    return render_template('dashboard.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
