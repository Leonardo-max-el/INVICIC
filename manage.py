import os
import sys

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'INVIC_APP.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            from django.apps import AppConfig
        except ImportError:
            raise
    execute_from_command_line(sys.argv)
