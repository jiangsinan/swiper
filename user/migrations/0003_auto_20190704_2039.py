# Generated by Django 2.2.3 on 2019-07-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='location',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='nickname',
            field=models.CharField(max_length=32, null=True),
        ),
    ]