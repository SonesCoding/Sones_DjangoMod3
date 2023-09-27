from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return self.name
    
    
class Quote(models.Model):
    name = models.CharField(max_length=50)
    Qtext = models.TextField()
    Author = models.ManyToManyField(Author)
    
    def __str__(self):
        return self.name + ", " + str(list(self.Author.all())[0]) #since the relationship is many to many i access manager and make it a list then just grab the first element. 
    #----thank you - eve----
    
class Star(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    color = models.TextField(max_length=100)
    Quote = models.ManyToManyField(Quote)
    
    def __str__(self) -> str:
        return self.name
    
#class Tag(models.Model):
    #name = 