#!/usr/bin/env python
import os
import sys
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
name = env('DJANGO_SETTINGS_MODULE') if env('DJANGO_SETTINGS_MODULE') else "blog.production"
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{name}")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
