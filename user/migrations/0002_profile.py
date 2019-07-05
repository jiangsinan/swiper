# Generated by Django 2.2.3 on 2019-07-04 20:17

from django.db import migrations, models
import lib.orm


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('bj', '北京'), ('sz', '深圳'), ('sh', '上海')], max_length=64)),
                ('min_distance', models.IntegerField(default=1)),
                ('max_distance', models.IntegerField(default=10)),
                ('min_dating_age', models.IntegerField(default=18)),
                ('max_dating_age', models.IntegerField(default=81)),
                ('dating_sex', models.IntegerField(choices=[(0, '全部'), (1, '男'), (2, '女')], default=0)),
                ('vibration', models.BooleanField(default=True)),
                ('only_matche', models.BooleanField(default=True)),
                ('auto_play', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'profiles',
            },
            bases=(models.Model, lib.orm.ModelToDictMixin),
        ),
    ]
