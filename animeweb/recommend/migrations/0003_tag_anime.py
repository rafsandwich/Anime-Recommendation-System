# Generated by Django 4.0 on 2022-02-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0002_review_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=5)),
                ('episodes', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('picture', models.CharField(max_length=200)),
                ('tags', models.ManyToManyField(to='recommend.Tag')),
            ],
        ),
    ]