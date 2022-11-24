from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    short_name = db.Column(db.String(255), nullable=False)
    overall = db.Column(db.Integer(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    height_cm = db.Column(db.Integer(), nullable=False)
    weight_kg = db.Column(db.Integer(), nullable=False)
    # club_name = db.Column(db.Integer(), nullable=False)
    # club_position = db.Column(db.String(5), nullable=False)
    # club_jersey_number = db.Column(db.Integer(), nullable=True)
    # nationality_name = db.Column(db.String(255), nullable=False)
    # preferred_foot = db.Column(db.String(5), nullable=False)
    # pace = db.Column(db.Integer(), nullable=True)
    # shooting = db.Column(db.Integer(), nullable=True)
    # passing = db.Column(db.Integer(), nullable=True)
    # dribbling = db.Column(db.Integer(), nullable=True)
    # defending = db.Column(db.Integer(), nullable=True)
    # player_face_url = db.Column(db.String(100), nullable=False)
    # club_logo_url = db.Column(db.String(100), nullable=False)
    # club_flag_url = db.Column(db.String(100), nullable=False)
    # nation_logo_url = db.Column(db.String(100), nullable=False)
    # nation_flag_url = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return{
            'short_name' : self.short_name,
            'overall' : self.overall,
            'age' : self.age,
            'height_cm' : self.height_cm,
            'weight_kg' : self.weight_kg
            # 'club_name' : self.club_name,
            # 'club_position' : self.club_position,
            # 'club_jersey_number' : self.club_jersey_number,
            # 'nationality_name' : self.nationality_name,
            # 'preferred_foot' : self.preferred_foot,
            # 'pace' : self.pace,
            # 'shooting' : self.shooting,
            # 'passing' : self.passing,
            # 'dribbling' : self.dribbling,
            # 'defending' : self.defending,
            # 'player_face_url' : self.player_face_url,
            # 'club_logo_url' : self.club_logo_url,
            # 'club_flag_url' : self.club_flag_url,
            # 'nation_logo_url' : self.nation_logo_url,
            # 'nation_flag_url' : self.nation_flag_url
        }
