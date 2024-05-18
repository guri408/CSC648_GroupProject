from werkzeug.security import check_password_hash

# Replace these values with the actual hashed password and plaintext password
hashed_password = "$2b$12$LZG28ZuxFp4MtFH6i2E41OrzJEKW0edydn05ISy4.ivg42qKjEz/q"
password = "12345678"  # Replace with the actual password

try:
    if check_password_hash(hashed_password, password):
        print("Password matches.")
    else:
        print("Password does not match.")
except ValueError as e:
    print(f"Error in password hash check: {e}")

