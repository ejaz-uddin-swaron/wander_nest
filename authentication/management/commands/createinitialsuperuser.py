from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create initial superuser without prompt'

    def handle(self, *args, **kwargs):
        # Check if a superuser named 'admin' already exists
        if not User.objects.filter(username='admin').exists():
            # Create the superuser with username, email and password
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Superuser created: admin / admin123'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
