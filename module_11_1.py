import requests

requests.get('https://github.com')
response = requests.get('https://github.com')
response.status_code
if response.status_code == 200:
    print('Успешно')
elif response.status_code == 404:
    print('Произошла ошибка')

data = {'key': 'value'}
response = requests.post('https://github.com', data=data)
print(response.text)

import matplotlib.pyplot as plt

x = [3, 8, 1, 6]
y = [28, 3, 32, 40]
plt.plot(x, y)
plt.show()

from PIL import Image
image = Image.open ("buildings.jpg")
image.show()
