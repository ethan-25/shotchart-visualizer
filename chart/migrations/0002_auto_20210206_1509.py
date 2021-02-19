# Generated by Django 3.1.4 on 2021-02-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=200)),
                ('season', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Input',
        ),
    ]
