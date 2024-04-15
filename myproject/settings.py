from __future__ import annotations

INSTALLED_APPS = ["myproject"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}
