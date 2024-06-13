from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine, Base
from models.user import User, Role
from schemas.user import UserCreate, User as UserSchema, Role as RoleSchema
from cryptography.fernet import Fernet
from config.settings import SECRET_KEY


Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    fernet = Fernet(SECRET_KEY)
    hashed_password = fernet.encrypt(
        user.password.encode()).decode()  # Cifrar el password

    db_user = User(email=user.email, name=user.name,
                   hashed_password=hashed_password, role_id=2)  # Default role as user
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/users/{user_id}/role/{role_id}", response_model=UserSchema)
def update_user_role(user_id: int, role_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")

    db_user.role_id = role_id
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/", response_model=list[UserSchema])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).join(Role).all()
    return users
