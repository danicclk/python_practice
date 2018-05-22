# Users Table
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    experience_level_id = db.Column(db.Integer, db.ForeignKey('experience_levels.id'))
    career_track_id = db.Column(db.Integer, db.ForeignKey('career_tracks.id'))
    # Users.job association
    bookmarks = db.relationship('Tags', secondary=bookmarks, lazy='subquery',
        backref=db.backref('users', lazy=True))
    

# Jobs Table
class Job(db.Model):
    __tablename__ = 'jobs'
    job_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # Not sure the one below
    body = db.Column(db.Text)
    # Not sure about the one below, this one is a many-to-many with the jobs
    users = db.relationship('User', backref='job', lazy='dynamic')
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))


# Resources Table
class Resource(db.Model):
    __tablename__ = 'resources'
    resource_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64), unique=True)

    # Not sure about the one below, this one is a many-to-many with the jobs
    users = db.relationship('User', backref='resource', lazy='dynamic')

# Companies Table
class Company(db.Model):
    __tablename__ = 'companies'
    company_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    jobs = db.relationship('Job', backref='company', lazy='dynamic')


# Skills Table
class Skill(db.Model):
    __tablename__ = 'Skills'
    skill_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # Not sure about the one below, this one is a many-to-many with the jobs
    jobs = db.relationship('Job', backref='skill', lazy='dynamic')


# Association between Job and User Tables, User.job 
bookmarks = db.Table('bookmarks',
    db.Column('job_id', db.Integer, db.ForeignKey('job_id'), primary_key=True), 
    db.Column('user_id', db.ForeignKey('user._id'), primary_key=True)
    )


# Association between Skill and User Tables, User.skill 
knows = db.Table('knows',
    db.Column('skill_id', db.Integer, db.ForeignKey('skill_id'), primary_key=True), 
    db.Column('user_id', db.ForeignKey('user._id'), primary_key=True)
    )


# Association between Resources and User Tables, User.resources 
knows = db.Table('knows',
    db.Column('resource_id', db.Integer, db.ForeignKey('resource_id'), primary_key=True), 
    db.Column('user_id', db.ForeignKey('user._id'), primary_key=True)
    )
