# Generated by Django 2.2.7 on 2019-11-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myblog',
            name='myimage',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
