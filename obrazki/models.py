from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Rectangle(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=7)
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return f"Rectangle {self.id} ({self.width}x{self.height})"

class Picture(models.Model):
    name = models.CharField(max_length=100)
    rectangles = models.ManyToManyField(Rectangle)
    size_x = models.IntegerField()
    size_y = models.IntegerField() 
    editors = models.ManyToManyField("auth.User")
    description = models.TextField(blank=True, default="", null=True)
    pub_date = models.DateTimeField('date published', blank=False, null=False, default=None)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name