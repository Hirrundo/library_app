from datetime import datetime, timedelta


from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from jose import jwt,JOSEError
# from dotenv import load_dotenv
from models import User
import settings
# load_dotenv()


pwd_context=PasswordHash.recommended()

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db:Session,username:str):
   return db.query(User).filter(User.username == username).first()

def create_accsess_token(data:dict)->str:
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=30)
    to_encode.update({'exp':expire})
    encode_jwt=jwt.encode(
    to_encode, settings.SECRET_KEY, settings.ALGORITHM
        )
    return encode_jwt




def authenticate_user(db:Session, 
                     username:str,
                     password:str
                     ):
    user=get_user(db,username)
    if not user:
        return False
    if not verify_password(password,user.password_hash):
        return False
    return user

def decode_access_token(token:str):
    try:
        payload=jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM])
        return payload
    except JOSEError:
        return None






