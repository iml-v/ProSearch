from django.db import models
#from django.contrib.auth import User

class Query(models.Model):
	username = models.TextField(max_length=20)
   	Query = models.TextField(default="This is default query",null=False,max_length=1000)
    #created = models.DateTimeField(auto_add_now=True)
    #id = models.AutoField(primary_key=True,)

    	#def __str__(self):
    	#	return "%&" username

    	