# Generated by Django 3.1.1 on 2022-03-04 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frontend_app', '0006_auto_20220207_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='company_name',
        ),
        migrations.AddField(
            model_name='password',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.FileField(upload_to='media', verbose_name='upload an image'),
        ),
    ]