from django.db import models


class City(models.Model):
    name = models.CharField(max_length=40)

    def to_excel(self):
        return self.name

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=40)
    city = models.ForeignKey(City, null=True, on_delete=models.CASCADE, related_name='publishers')

    def to_excel(self):
        return self.name

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')

    def to_excel(self):
        return self.title

    def __str__(self):
        return self.title
