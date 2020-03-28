import subprocess
from sqlalchemy.exc import OperationalError
from app.controller import game
from app.config import db
from app.model import Record


if __name__ == '__main__':
	cmd = "venv\\Scripts\\activate"
	subprocess.call(cmd, shell=True)
	db.app = game
	db.create_all()
	try:
		Record.__table__.create(db.engine)
	except OperationalError:
		Record.__table__.drop(db.engine)
		Record.__table__.create(db.engine)

	game.run('localhost', port=80, debug=True)
	cmd = "venv\\Scripts\\deactivate"
	subprocess.call(cmd, shell=True)