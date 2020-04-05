# Generated by Django 2.1.5 on 2020-04-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('pub_date', models.DateField()),
                ('body', models.TextField(max_length=600)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
