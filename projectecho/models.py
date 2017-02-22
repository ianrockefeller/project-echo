from __future__ import unicode_literals

from django.db import models

# enforce unique as long as the entire model does not need to be unique

class Address(model.Models):
  street = models.TextField()
  city = models.TextField()
  state = models.TextField()
  zipcode = models.CharField(max_length=5)

#  class Meta:
#    unique_together = ('street', 'city', 'state', 'zipcode')

class Genre(model.Models):
  name = models.TextField(unique=True)

class Venue(model.Models):
  name = model.TextField()
  address = models.ForeignKey(Address, on_delete=models.CASCADE)

#  class Meta:
#    unique_together = ('name', 'address')

class Band(model.Models):
  TYPE_CHOICES = (
    ('O', 'Original'),
    ('C', 'Cover'),
    ('B', 'Both'),
  )

  name = models.TextField()
  address = models.ForeignKey(Address, on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre, on_delete=modela.CASCADE)
  type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='O')

class Promoter(model.Models):
  first_name = models.TextField()
  last_name = models.TextField()
  address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Event(model.Models):
  name = models.TextField()
  venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
  date = models.DateField()
  bands = model.ManyToManyField(Band, blank=True)
  promoter = model.ForeignKey(Promoter, on_delete=models.CASCADE)

