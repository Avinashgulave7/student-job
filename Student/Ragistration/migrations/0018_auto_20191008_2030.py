# Generated by Django 2.2.4 on 2019-10-08 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ragistration', '0017_auto_20191008_1849'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ragister',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
