# Generated by Django 4.2.10 on 2024-05-28 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_qualifications_owner_alter_skills_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualifications',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='skills',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to=settings.AUTH_USER_MODEL),
        ),
    ]
