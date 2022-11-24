from flask import Blueprint, render_template, request, redirect
from app.models import db, Player
import pandas as pd

ui_bp = Blueprint(
   'ui_bp', __name__,
   template_folder='templates',
   static_folder='static'
)


@ui_bp.route('/')
def home():
   return render_template("home.html")


@ui_bp.route('/players', methods=['GET', 'POST'])
def import_players():
   # TO DO
   return render_template('players.html')


# Import multiple players
@ui_bp.route('/players/import')
def add_players():
   title = 'Import Datasets'
   return render_template('upload_players.html', title=title)


@ui_bp.route('/datasets/import/upload_file', methods=['POST'])
def upload_file():
   # get the uploaded file
   uploaded_file = request.files['file']
   # if not empty
   if uploaded_file.filename != '':
       # set the file path
       # file_path = os.path.join(config.UPLOAD_FOLDER, uploaded_file.filename)
       # save the file
       uploaded_file.save(uploaded_file.filename)
       parse_csv_players(uploaded_file.filename)
   return redirect('/players/import')


def parse_csv_players(file_path):
    # Use Pandas to parse the CSV file
    csv_data = pd.read_csv(file_path)
    # Loop through the rows and create a Student object for each row
    for i, row in csv_data.iterrows():
        player = Player(
            short_name=row['short_name'],
            overall=row['overall'],
            age=row['age'],
            height_cm=row['height_cm'],
            weight_kg=row['weight_kg']
        )
        # Insert each grade into db
        db.session.add(player)
    db.session.commit()


@ui_bp.route('/players')
def list_players():
    players = Player.query
    return render_template('players.html', title='Players', players=players)


@ui_bp.route('/api/players')
def players_all():
    return {'data': [player.to_dict() for player in Player.query]}

 