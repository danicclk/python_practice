Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> r = requests.get('https://jobs.github.com/positions.json?description=python&location=new+york')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    r = requests.get('https://jobs.github.com/positions.json?description=python&location=new+york')
NameError: name 'requests' is not defined
>>> import requests
>>> 
