# Generated by Django 2.2.6 on 2020-03-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]