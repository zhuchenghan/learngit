# Generated by Django 2.1.8 on 2019-10-27 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_dbs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbs',
            name='db_platform',
        ),
        migrations.AddField(
            model_name='platform',
            name='platform_db',
            field=models.ManyToManyField(to='polls.dbs'),
        ),
    ]