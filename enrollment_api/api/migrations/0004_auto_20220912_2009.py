# Generated by Django 2.2.16 on 2022-09-12 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220912_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='parentId',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
    ]
