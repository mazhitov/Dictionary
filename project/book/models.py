from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField('Контактное имя', max_length=50)

    def __str__(self):
        return self.name

    def all_phones_to_string(self):
        return ", ".join([phone.phone for phone in self.phones.all()])


class Phone(models.Model):
    phone = models.CharField('Телефон', max_length=50)
    contact = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="phones")

    def __str__(self):
        return self.phone
