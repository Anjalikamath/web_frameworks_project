# Generated by Django 2.1.7 on 2019-04-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_id', models.IntegerField()),
                ('b_name', models.CharField(max_length=100)),
                ('b_author', models.CharField(max_length=100)),
                ('b_publisher', models.CharField(max_length=100)),
                ('b_year', models.IntegerField()),
                ('b_img_src', models.CharField(max_length=100)),
                ('b_describe', models.CharField(max_length=2000)),
            ],
        ),
    ]
