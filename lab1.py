import requests
response=requests.get('https://github.com/lindaZ1/cmput404lab1/raw/master/lab1.py')
print(response.text)
