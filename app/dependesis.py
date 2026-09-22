from fastapi import Depends, HTTPException,Request, status
from jose import jwt,JWTError
from database import SessionLocal
from models import User
import settings
from sqlalchemy.orm import Session
from auth import get_user


def get_db():
        db=SessionLocal()
        try:
            yield db

        except Exception as e:
                db.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f'Нет соединения с бд:{str(e)}'
                )
        finally:
            db.close()

def get_token(request:Request):
    token=request.cookies.get('access_token')
    if not token:
        auth_header=request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer'):
            token=auth_header[8:]
    print(token)
    return token

def get_current_user(token:str=Depends(get_token), db:Session=Depends(get_db)):
    try:
        payLoad=jwt.decode(token,settings.secret_key,settings.algorytm)
        username=payLoad.get('sub')
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='token does not contain user into'
            )
        token_data=username
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='invalid token'
            )
    user=get_user(db,username)
    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail='user not found'
        )
    return user

def get_current_active_user(current_user):
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='User is inactivate'
        )
    return current_user

def get_admin_user(current_user):
    if current_user.role !='admin':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Admin access required')
    return current_user

def get_librarian_user(current_user):
    if current_user.role not in ['librarian','admin']:
         raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail='librarian access required')
    return current_user
