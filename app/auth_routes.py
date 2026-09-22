from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from shemas import LoginRequest,Token,UserResponse,PasswordChangeRequest,UserCreate
from models import User
from auth import authenticate_user,create_accsess_token,get_password_hash,verify_password
from dependesis import get_db,get_current_active_user,get_admin_user


router=APIRouter()

@router.post("/login", response_model=Token)
def login(
 login_data: LoginRequest,
 db: Session = Depends(get_db)
):
    db_user=authenticate_user(db,login_data.username,login_data.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Неверный логин или пароль',
            headers={'WWW-Authenticate':'Bearer'}
        )
    access_token=create_accsess_token(data={'sub':db_user.username,
                                            'role':db_user.role})
    return{
        'access_token':access_token,
        'token-type':'bearer'
    }