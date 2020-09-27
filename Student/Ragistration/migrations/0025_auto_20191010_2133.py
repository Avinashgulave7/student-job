# Generated by Django 2.2.4 on 2019-10-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ragistration', '0024_remove_contact_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('feedback', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]