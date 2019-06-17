from models.database import db


class SubCounties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # db.relationship('Ward', backref='sub_county', lazy='joined')

    def __init__(self, name):
        self.name = name


class Wards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    sub_county = db.Column(db.Integer, db.ForeignKey('sub_counties.id'), nullable=False,)

    def __init__(self, name, sub_county):
        self.name = name
        self.sub_county = sub_county


class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ward = db.Column(db.Integer, db.ForeignKey('wards.id'), nullable=False)

    def __init__(self, name, wards):
        self.name = name
        self.wards = wards


class SubLocations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Villages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    sub_location = db.Column(db.Integer, db.ForeignKey('sub_locations.id'), nullable=False)

    def __init__(self, name, sub_location):
        self.name = name
        self.sub_location = sub_location
