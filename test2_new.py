import requests


response = requests.get('https://github.com/alkunit/slurm1/tree/master.test1.py')
txt = response.content

print(txt)

# try:
#     with open(r'https://github.com/alkunit/slurm1/tree/master.test1.py', 'r') as f:
#         L = f.readlines()
#         print(L[0])
# except FileNotFoundError:
#     print("Не удалось проверить версию приложения")