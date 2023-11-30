# Generated by Django 4.2.6 on 2023-11-10 14:59

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_remove_case_description_items_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case_related',
            old_name='items',
            new_name='for_case',
        ),
        migrations.AddField(
            model_name='case_related',
            name='item',
            field=models.FileField(blank=True, null=True, upload_to=myapp.models.filepath),
        ),
    ]