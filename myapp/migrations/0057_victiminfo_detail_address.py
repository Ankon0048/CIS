# Generated by Django 4.2.7 on 2023-12-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0056_emergency"),
    ]

    operations = [
        migrations.AddField(
            model_name="victiminfo",
            name="detail_address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
