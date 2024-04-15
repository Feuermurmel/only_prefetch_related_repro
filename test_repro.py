from __future__ import annotations

import pytest

from myproject.models import Building
from myproject.models import Restaurant
from myproject.models import City


@pytest.mark.parametrize('qs', [
    Building.objects.prefetch_related("restaurant", "city"),
    Building.objects.only("street_name").prefetch_related("restaurant"),
    Building.objects.only("street_name").prefetch_related("city", "restaurant"),
    Building.objects.only("street_name").prefetch_related("restaurant", "city")
])
def test_repro(db, django_assert_num_queries, qs):
    Restaurant.objects.create(
        name="",
        building=Building.objects.create(
            city=City.objects.create(name=""), street_name="", street_no=""
        ),
    )

    result = list(qs)

    with django_assert_num_queries(0):
        result[0].restaurant
