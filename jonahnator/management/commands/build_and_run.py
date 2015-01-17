import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Custom management command to build frontend"""
    help = 'Custom management to build frontend'

    def handle(self, *args, **options):
        # save current working dir
        base_path = os.getcwdu()
        frontend_path = base_path + '/frontend'

        os.chdir(frontend_path)
        os.system('npm run build')
        os.chdir(frontend_path + '/..')
        os.system('./manage.py runserver')

        # restore current working dir
        os.chdir(base_path)
