# Generated by Django 2.0.5 on 2018-05-22 14:39
from django.db import migrations
from django.contrib.auth.models import User

def crear_usuario_administrador(apps, schema_editor):
    User.objects.create_superuser(username='admin', password='asdasd123', email='')


class Migration(migrations.Migration):

    dependencies = [
        ('copatic', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_usuario_administrador, migrations.RunPython.noop),
    ]
