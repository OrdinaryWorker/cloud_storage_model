# Generated by Django 2.2.16 on 2022-09-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20220913_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
