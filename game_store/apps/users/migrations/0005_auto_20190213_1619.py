# Generated by Django 2.1.5 on 2019-02-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190213_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[(0, 'Player'), (1, 'Developer')], default='', max_length=1),
        ),
    ]
