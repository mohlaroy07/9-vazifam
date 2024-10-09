from django.db import models

class Category(models.Model):
    id= models.IntegerField()
    title = models.CharField(max_length=150)
    name = models.CharField(max_length=150)    


    def __str__(self) -> str:
        return f"{self.title} : {self.name}"
    
    
class Ad(models.Model):
    title = models.CharField(max_length=150)
    owner = models.CharField(max_length=150)
    description = models.TextField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   
    
    
    def __str__(self):
        return f'{self.title} : {self.description}'