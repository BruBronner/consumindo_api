import requests

print('github users\n') #\n (sep)

username = input('qual é o nome do usuário? ')

url = f'https://api.github.com/users/{username}'
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f'Nome Completo:{data["name"]}')
    print(f'Bio:{data["Bio"]}')
    print(f'location:{data["location"]}')
    print(f'Seguindo:{data["following"]}')
    
else:
    print('não foi possivel encontrar o usuário')