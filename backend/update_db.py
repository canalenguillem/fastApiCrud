# update_db.py
from config.database import Base, engine, SessionLocal
from models.user import User, Role
from sqlalchemy.exc import IntegrityError

# Crear todas las tablas
Base.metadata.create_all(engine)


def init_db():
    session = SessionLocal()

    try:
        # Crear roles por defecto si no existen
        if session.query(Role).count() == 0:
            admin_role = Role(name="admin")
            user_role = Role(name="user")
            session.add(admin_role)
            session.add(user_role)
            session.commit()
    except IntegrityError:
        session.rollback()
        print("Roles 'admin' y 'user' ya existen en la base de datos.")

    session.close()


if __name__ == "__main__":
    # Eliminar y crear la tabla de nuevo
    User.__table__.drop(engine)
    Role.__table__.drop(engine)
    Base.metadata.create_all(engine)
    init_db()
