from app.config import db


class Record(db.Model):
  __tablename__ = 'record'
  id = db.Column(db.String(30), primary_key=True)
  score = db.Column(db.Integer, nullable=False, default=0)

  def save(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find(cls, id):
    return Record.query.filter(cls.id == id).first()