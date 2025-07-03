from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class Record(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tall = models.IntegerField()
    weight = models.IntegerField()
    address = models.CharField(max_length=500)
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return self.first_name + " " + self.last_name
    