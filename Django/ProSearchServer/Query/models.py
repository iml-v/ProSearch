from django.db import models
from .name_generator import generator
	
class Questions(models.Model):
    #qvalue = models.ForeignKey(QueryM,on_delete=models.CASCADE,null=False)
    question = models.TextField(default="hi")
    name = models.TextField(default="yo")
    query = models.TextField(default="mama")

    def save(self, *args, **kwargs):
        self.question =  generator(self.query)
        
        super(Questions, self).save(*args, **kwargs)
    	