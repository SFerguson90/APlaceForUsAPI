from extensions import db


class Dog(db.Model):

    __tablename__ = 'dog'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200))
    age = db.Column(db.Integer, default=1)
    color = db.Column(db.String(30))
    cat_friendly = db.Column(db.Boolean(), default=False)
    small_dog_friendly = db.Column(db.Boolean(), default=False)
    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'age': self.age,
            'color': self.color,
            'cat_friendly': self.cat_friendly,
            'small_dog_friendly': self.small_dog_friendly,
            'user_id': self.user_id
        }

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_publish=True).all()

    @classmethod
    def get_by_id(cls, dog_id):
        return cls.query.filter_by(id=dog_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
