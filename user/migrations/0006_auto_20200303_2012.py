# Generated by Django 3.0.2 on 2020-03-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200303_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='auther',
            field=models.CharField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
    ]