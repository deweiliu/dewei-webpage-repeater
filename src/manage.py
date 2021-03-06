#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time
from repeater.views import get_time


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'webpage_repeater.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # record deployment time
    os.environ['deploy_time'] = get_time.value()

    main()
