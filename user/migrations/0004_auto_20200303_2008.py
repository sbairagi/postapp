# Generated by Django 3.0.2 on 2020-03-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200303_2006'),
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
            field=models.CharField(max_length=20, null=True),
        ),
    ]
