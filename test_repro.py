from __future__ import annotations

from myproject.models import Building
from myproject.models import Restaurant
from myproject.models import City


def test_repro(db, django_assert_num_queries):
    Restaurant.objects.create(
        name="",
        building=Building.objects.create(
            city=City.objects.create(name=""), street_name="", street_no=""
        ),
    )

    # qs = Building.objects.prefetch_related("restaurant", "city")
    # qs = Building.objects.only("street_name").prefetch_related("restaurant")
    # qs = Building.objects.only("street_name").prefetch_related("city", "restaurant")
    qs = Building.objects.only("street_name").prefetch_related("restaurant", "city")
    result = list(qs)

    with django_assert_num_queries(0):
        result[0].restaurant
