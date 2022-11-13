# Generated by Django 4.1.2 on 2022-10-30 23:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0021_alter_post_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='mod_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date modified'),
        ),
        migrations.AddField(
            model_name='album',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]