# Generated by Django 4.0 on 2021-12-13 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='short',
            options={'ordering': ['-created_at'], 'verbose_name': 'URL'},
        ),
        migrations.AlterModelTable(
            name='short',
            table='url_shortene2r',
        ),
    ]
