import requests as r 

req = r.post('http://127.0.0.1:8000/auth/jwt/login/', {
        'username': 'admin',
        'password': 'admin'
    })

print(req.json())