from django.db import models
import string

class CommonFields(models.Model):
    added_by = models.CharField(max_length=30)
    modified_by = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Student(CommonFields):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_name(self):
        return (self.first_name.capitalize() + ' ' + self.last_name.capitalize())

    def uppercase_name(self):
        return (self.first_name.upper() + ' ' + self.last_name.upper())


