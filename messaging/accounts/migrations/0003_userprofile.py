# Generated by Django 2.1.1 on 2018-10-06 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('accounts', '0002_auto_20180924_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
