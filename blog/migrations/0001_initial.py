# Generated by Django 2.1.5 on 2020-06-13 09:38

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
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
