# Generated by Django 2.2 on 2019-05-23 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0013_auto_20190523_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorreport',
            name='error',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
