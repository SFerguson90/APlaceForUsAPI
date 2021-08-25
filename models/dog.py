from extensions import db

dog_list = []


def get_last_id():
    """
        Function used to find the last ID, while creating a new Dog object
    """
    if dog_list:
        last_dog = dog_list[-1]
    else:
        return 1
    return last_dog.id + 1


class Dog(db.Model):

    __tablename__ = 'dog'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    age = db.Column(db.Integer, default=1)
    color = db.Column(db.String(50))
    cat_friendly = db.Column(db.Boolean(), default=False)
    small_dog_friendly = db.Column(db.Boolean(), default=False)
    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
