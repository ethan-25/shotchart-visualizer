# Generated by Django 3.1.4 on 2021-02-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0002_auto_20210206_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartinfo',
            name='season_type',
            field=models.CharField(choices=[('Regular Season', 'Regular Season'), ('Playoffs', 'Playoffs')], default='Regular Season', max_length=50),
        ),
        migrations.AlterField(
            model_name='chartinfo',
            name='player_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='chartinfo',
            name='season',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='chartinfo',
            name='team',
            field=models.CharField(max_length=3),
        ),
    ]
