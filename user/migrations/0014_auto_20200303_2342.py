# Generated by Django 3.0.2 on 2020-03-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20200303_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='allposts',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='auther',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
