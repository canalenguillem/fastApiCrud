from cryptography.fernet import Fernet

# Genera una clave y guárdala en un lugar seguro
key = Fernet.generate_key()
print(f"Guardar esta clave en un lugar seguro: {key.decode()}")
