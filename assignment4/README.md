# Assignment Requirements

1. Implement a repository for your project/API
2. Translate your API into one that uses the Django REST Framework
3. Use the built-in Django O/RM rather than the Repository we hand-crafter [sic] previously

## Requirements Interpretation
1. (1a) Create a Django project that uses O/RM and utilizes db.sqlite3 using the same themes as assignment 2 and 3.
2. (2a) Create a separate Django API project that uses the REST Framework and replicate what you did in step 1a but using this different method instead. ALSO create a separate repository for the API to talk to.

# Description
This section will describe what each file name does and which part of the assignment requirements it aligns to.

## 1a O/RM with Respository
The O/RM architecture for this version of the assignment is found in the files `/orm/models.py` and `assignment4/settings.py`. This method relies on using the Django Shell method for inserting, updating, and deleting data stored in the `db.sqlite3` respository.

In `/orm/models.py` , three classes (User, Session, and Event) were developed based on the ERD from Assignment 2 shown below:

![ERD for users and items](/assignment2/class-erd.png)

```python
from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    email = models.EmailField(unique=True)
    isadmin = models.BooleanField(default=False)
    isreporter = models.BooleanField(default=False)
    isanalyst = models.BooleanField(default=False)
    isviewer = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Session(models.Model):
    sessionid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    sessionkey = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.sessionkey
    
class Event(models.Model):
    eventid = models.AutoField(primary_key=True)
    sessionid = models.ForeignKey(Session, on_delete=models.CASCADE)
    itemid = models.CharField(max_length=100)
    eventtime = models.DateTimeField(auto_now_add=True)
    eventtype = models.CharField(max_length=100)

    def __str__(self):
        return self.eventid
```
By using the following code in the terminal, one can succesfully perform all CRUD functions through additional commands.

```
python manage.py shell
```

## 2a API with REST Framework
The RESTful API version of this assignment is found in these files: `/api/models.py` , `/api/seralizers.py` , `/api/urls.py` ,  `/api/views.py` , `/assignment4/settings.py` , and `/assignment4/urls.py` . This pattern reliably executes CRUD functions by submitting forms in http://127.0.0.1:8000/users , http://127.0.0.1:8000/sessions , and http://127.0.0.1:8000/events

The class models in models.py are the exact same in the O/RM version.

# Resources Used
<https://www.geeksforgeeks.org/getting-started-with-django/>

<https://www.geeksforgeeks.org/django-orm-inserting-updating-deleting-data/?ref=gcse>

<https://www.geeksforgeeks.org/how-to-create-a-basic-api-using-django-rest-framework/>

<https://www.django-rest-framework.org/tutorial/quickstart/>

<https://www.shecodes.io/athena/9722-implement-repository-for-model-with-django-rest-framework#google_vignette>

<https://www.reddit.com/r/django/comments/d0596f/orm_vs_orm_repository_pattern/>

<https://medium.com/@slowmoe329/repository-design-pattern-in-django-a-clean-and-scalable-approach-a94d2645fd77>