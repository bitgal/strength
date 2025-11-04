import bcrypt

def hash_password(password:str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

def verify_password(password:str, hashed: str) -> bool:
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(password.encode('utf-8'))
    print(hashed.encode('utf-8'))
    
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

t = hash_password("123123123")
print(t)
print(verify_password("123123123", t))