# Generated by Django 2.2.5 on 2020-02-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytweets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('tweet', models.ManyToManyField(to='mytweets.Tweet')),
            ],
        ),
    ]
