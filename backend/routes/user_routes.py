from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.user import User as SQLAlchemyUser, Role
from schemas.user import UserCreate, User as PydanticUser, Role as RoleSchema, UserDeleteResponse
from routes.auth import get_current_user
from cryptography.fernet import Fernet
from config.settings import SECRET_KEY

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

fernet = Fernet(SECRET_KEY)


@router.post("/", response_model=PydanticUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = fernet.encrypt(
        user.password.encode()).decode()  # Cifrar el password
    db_user = SQLAlchemyUser(email=user.email, name=user.name,
                             hashed_password=hashed_password, role_id=2)  # Default role as user
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/{user_id}", response_model=PydanticUser)
def read_user(user_id: int, db: Session = Depends(get_db), current_user: SQLAlchemyUser = Depends(get_current_user)):
    db_user = db.query(SQLAlchemyUser).filter(
        SQLAlchemyUser.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}/role/{role_id}", response_model=PydanticUser)
def update_user_role(user_id: int, role_id: int, db: Session = Depends(get_db), current_user: SQLAlchemyUser = Depends(get_current_user)):
    db_user = db.query(SQLAlchemyUser).filter(
        SQLAlchemyUser.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")

    db_user.role_id = role_id
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/", response_model=list[PydanticUser])
def list_users(db: Session = Depends(get_db), current_user: SQLAlchemyUser = Depends(get_current_user)):
    users = db.query(SQLAlchemyUser).all()
    return users


@router.delete("/{user_id}", response_model=UserDeleteResponse)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: SQLAlchemyUser = Depends(get_current_user)):
    db_user = db.query(SQLAlchemyUser).filter(
        SQLAlchemyUser.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    return UserDeleteResponse(message="User deleted successfully")
