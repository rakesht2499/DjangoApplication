# Generated by Django 2.2.6 on 2020-04-10 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentcode', models.TextField()),
                ('adminno', models.TextField()),
                ('studentname', models.TextField()),
                ('slassname', models.TextField()),
                ('section', models.TextField()),
                ('dob', models.TextField()),
                ('result', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]