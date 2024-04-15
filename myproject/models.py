from __future__ import annotations

from django.db.models import DO_NOTHING
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import OneToOneField
from django.db.models import TextField


class City(Model):
    name = TextField()


class Building(Model):
    city = ForeignKey(City, on_delete=DO_NOTHING)

    street_name = TextField()
    street_no = TextField()


class Restaurant(Model):
    building = OneToOneField(Building, on_delete=DO_NOTHING)

    name = TextField()
