# Generated by Django 2.2.4 on 2019-10-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ragistration', '0021_auto_20191010_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact1',
        ),
    ]
