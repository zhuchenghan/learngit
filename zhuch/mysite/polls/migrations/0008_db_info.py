# Generated by Django 2.1.8 on 2019-11-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_remove_platform_platform_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='db_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_type', models.CharField(max_length=10)),
                ('db_name', models.CharField(max_length=10)),
                ('usename', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('port', models.IntegerField(default=3306)),
                ('platform_id', models.IntegerField()),
            ],
        ),
    ]
