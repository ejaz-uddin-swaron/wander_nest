from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create(
        username='admin',
        email='admin@example.com',
        is_staff=True,
        is_superuser=True,
        is_active=True,
        password=make_password('admin123')  # Set your password here
    )

class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),  # Adjust this if your last migration number is different
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
