# Generated by Django 3.0.2 on 2020-03-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.IntegerField()),
            ],
        ),
    ]
