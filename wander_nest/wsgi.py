import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wander_nest.settings')

application = get_wsgi_application()

# 🚨 One-day-only hack: auto-run DB migrations on Render startup
import django
from django.core.management import call_command

django.setup()
try:
    call_command('migrate', interactive=False)
    print("✅ Migrations applied successfully.")
except Exception as e:
    print("❌ Migration failed:", e)
