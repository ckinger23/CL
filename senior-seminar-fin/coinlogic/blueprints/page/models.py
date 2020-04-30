from coinlogic.extensions import db

class Firm(db.model):

    __tablename__ = 'firms'

    index = db.Column(db.String(200), primary_key = True)
    issue = db.Column(db.String(200))
    tclass = db.Column(db.String(200))
    cusip = db.Column(db.String(200))
    value = db.Column(db.String(200))
    sshp = db.column(db.String(200))
    sshpt = db.Column(db.String(200))
    investd = db.Column(db.String(200))
    otherman = db.Column(db.String(200))
    sole = db.Column(db.String(200))
    shared = db.Column(db.String(200))
    none = db.Column(db.String(200))

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(Firm, self).__init__(**kwargs)
