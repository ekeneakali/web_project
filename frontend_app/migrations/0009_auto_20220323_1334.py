# Generated by Django 3.1.1 on 2022-03-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend_app', '0008_auto_20220307_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='describe your product'),
        ),
        migrations.AlterField(
            model_name='video',
            name='content',
            field=models.TextField(verbose_name='describe your product'),
        ),
    ]