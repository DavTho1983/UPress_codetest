# Generated by Django 2.2 on 2019-05-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarcasm', '0003_auto_20190515_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='article_link',
            field=models.CharField(max_length=1000),
        ),
    ]
