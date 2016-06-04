"""
    Initialize Django environment

    just do:

        import tests.base.init
"""
import django
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chobie.settings")
django.setup()
