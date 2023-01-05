# Real estate rental Django Rest Framework


## Steps
- run ```docker-compose up --build``` for first time, then ```docker-compose up```

Once the docker is running, you can test the API below


### I'm sending an export of requests of the activity, file:
```Seazone.postman_collection.json```
just import to your postman and test all the endpoints of API

For super user, use this:
username = admin
password = mystrongpassword

feel free to create another user, using ```createsuperuser``` command inside docker


## Added Test Cases with APITestCase
just run insde docker:
```python manage.py test```