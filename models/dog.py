from extensions import db
from sqlalchemy import asc, desc, or_

class Dog(db.Model):

    __tablename__ = 'dog'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200))
    age = db.Column(db.Integer, default=1)
    color = db.Column(db.String(30))
    location = db.Column(db.String(40), default="Lubbock, TX")
    cat_friendly = db.Column(db.Boolean(), default=False)
    small_dog_friendly = db.Column(db.Boolean(), default=False)
    cover_image = db.Column(db.String(100), default=None)
    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

    @classmethod
    def get_all_published(cls, q, page, per_page, sort, order):
        
        keyword = '%{keyword}%'.format(keyword=q)

        if order == 'asc':
            sort_logic = asc(getattr(cls, sort))
        else:
            sort_logic = desc(getattr(cls, sort))


        return cls.query.filter(or_(cls.name.ilike(keyword),
                cls.description.ilike(keyword),
                cls.location.ilike(keyword)),
                cls.is_publish.is_(True)).order_by(sort_logic).paginate(page=page, per_page=per_page)

    @classmethod
    def get_by_id(cls, dog_id):
        return cls.query.filter_by(id=dog_id).first()

    @classmethod
    def get_all_by_user(cls, user_id, page, per_page, visibility='public'):

        query = cls.query.filter_by(user_id=user_id)

        if visibility == 'public':
            query = cls.query.filter_by(user_id=user_id, is_publish=True)
        elif visibility == 'private':
            query = cls.query.filter_by(user_id=user_id, is_publish=False)

        return query.order_by(desc(cls.created_at)).paginate(page=page, per_page=per_page)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
