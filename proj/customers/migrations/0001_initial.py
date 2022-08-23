# Generated by Django 4.0.3 on 2022-08-11 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(db_column='CustomerId', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, db_column='FirstName', max_length=128)),
                ('last_name', models.CharField(blank=True, db_column='LastName', max_length=128)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=512)),
            ],
        ),
    ]
