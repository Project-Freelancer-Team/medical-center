# Generated by Django 4.2.10 on 2024-05-28 14:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Tag'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='post_text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
