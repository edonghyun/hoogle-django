# Generated by Django 3.1.7 on 2021-03-03 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210303_1925'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='article',
            unique_together={('title', 'date')},
        ),
    ]
