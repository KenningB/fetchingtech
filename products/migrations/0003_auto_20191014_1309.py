# Generated by Django 2.2.6 on 2019-10-14 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191014_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variant',
            options={'ordering': ['product', 'name']},
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='parent',
            new_name='product',
        ),
        migrations.AlterUniqueTogether(
            name='variant',
            unique_together={('product', 'name')},
        ),
    ]