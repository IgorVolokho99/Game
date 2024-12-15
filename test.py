import bcrypt

password = '123'

password = password.encode('utf-8')

hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(rounds=5))

hashed_password = hashed_password.decode('utf-8')

print(hashed_password)
