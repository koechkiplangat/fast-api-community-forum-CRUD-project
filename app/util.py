from passlib.context import CryptContext
pwd_context =  CryptContext(schemes=["bcrypt"], deprecated="auto")

#Hashes the password being stored in db
def hash(password: str):
    hashed_password = pwd_context.hash(password)
    return hashed_password

# verify - used in login endpoint to make comparison of provided password (plain) to that stored in database
def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


