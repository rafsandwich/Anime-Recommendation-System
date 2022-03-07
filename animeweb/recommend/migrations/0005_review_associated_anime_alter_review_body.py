# Generated by Django 4.0 on 2022-03-07 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0004_alter_anime_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='associated_anime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recommend.anime'),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(max_length=2000),
        ),
    ]
