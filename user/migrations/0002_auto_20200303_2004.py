# Generated by Django 3.0.2 on 2020-03-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='allposts',
            field=models.TextField(null=True),
        ),
    ]
