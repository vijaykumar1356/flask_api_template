from uuid import uuid4
from flask import jsonify
from flask_restful import Resource
from flask_pydantic import validate
from pydantic import BaseModel, EmailStr
from typing import Optional, List

# local imports
from src.models import User
from src.utils import api_abort
from src.extentions import db


class UserCreate(BaseModel):
    first_name: str
    last_name: Optional[str]
    email: EmailStr
    password: str
    unique_id: str


class UserOut(UserCreate):
    id: int

    class Config:
        orm_mode = True


class UsersOut(BaseModel):
    users: List[UserOut]


class UserApi(Resource):

    def get(self, user_id: Optional[str] = None):
        try:
            if user_id:
                db_obj = User.query.filter(User.unique_id == user_id).first()
                if not db_obj:
                    raise Exception('User not found with given id !!')
                return jsonify(UserOut.from_orm(db_obj).dict())
            else:
                db_users = User.query.all()
                data = UsersOut(users=db_users)
                return jsonify(data.dict())
        except Exception as e:
            api_abort(400, message=str(e))

    @validate()
    def post(self, body: UserCreate):
        try:
            user_obj = User(**body.dict())
            user_obj['unique_id'] = uuid4().hex
            db.session.add(user_obj)
            db.session.commit()
            db.session.refresh(user_obj)
            return jsonify(UserOut.from_orm(user_obj).dict())

        except Exception as e:
            api_abort(400, message=str(e))

    def delete(self, user_id: int):
        try:
            db_obj = User.query.filter(User.id == user_id).first()
            if not db_obj:
                raise Exception('User not found with given id !!')
            db.session.delete(db_obj)
            db.session.commit()
            return {'message': 'user record deleted successfully !!'}

        except Exception as e:
            api_abort(400, message=str(e))
