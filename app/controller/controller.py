import json
from app.config import game
from app.model import Record
from flask import render_template, request, url_for, redirect


@game.route('/', methods=['GET'])
def index():
	return render_template("pages/index.html")

@game.route('/scores', methods=['GET'])
def scores():
	players = Record.query.all()
	return render_template("pages/scores.html", players=players)

@game.route('/record', methods=['POST'])
def record():
	player_dict = str(request.form.get('data'))
	player_dict = json.loads(player_dict)

	for key in player_dict.keys():
		record = Record.find(key)
		
		if not record:
			score = player_dict.get(key)
			record = Record(id=key, score=score)
		else:
			record.score = record.score + player_dict.get(key) 
		
		record.save()

	# return json.dumps(player_dict)
	return redirect(url_for('scores'))