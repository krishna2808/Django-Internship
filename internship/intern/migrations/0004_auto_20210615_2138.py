# Generated by Django 2.2.15 on 2021-06-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0003_auto_20210615_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='Posts/%Y/%m/%d'),
        ),
    ]
