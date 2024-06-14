from sqlalchemy.orm import Session
from sqlalchemy import delete, text
from config.database import engine, get_db
from models.user import Base, User, Role
from cryptography.fernet import Fernet
from config.settings import SECRET_KEY


def reset_database():
    # Iniciar sesión de la base de datos
    db: Session = next(get_db())

    # Eliminar todos los usuarios y roles
    db.execute(delete(User))
    db.execute(delete(Role))
    db.commit()
    print("All users and roles have been deleted.")

    # Reiniciar los IDs de las tablas
    db.execute(text("ALTER TABLE users AUTO_INCREMENT = 1"))
    db.execute(text("ALTER TABLE roles AUTO_INCREMENT = 1"))
    db.commit()
    print("IDs have been reset to 1.")

    # Crear roles
    admin_role = Role(name="admin")
    user_role = Role(name="user")
    db.add(admin_role)
    db.add(user_role)
    db.commit()
    print("Roles created: admin and user.")

    # Crear usuarios
    fernet = Fernet(SECRET_KEY)

    hashed_password_guillem = fernet.encrypt(b"guillem").decode()
    guillem_user = User(email="guillem@example.com", name="guillem",
                        hashed_password=hashed_password_guillem, role_id=admin_role.id)
    db.add(guillem_user)

    hashed_password_maria = fernet.encrypt(b"maria").decode()
    maria_user = User(email="maria@example.com", name="maria",
                      hashed_password=hashed_password_maria, role_id=user_role.id)
    db.add(maria_user)

    db.commit()
    print("Users created: guillem and maria.")


if __name__ == "__main__":
    reset_database()
    print("Database has been reset and initial data has been created.")
