# Generated by Django 4.1.5 on 2023-01-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contato", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contato",
            name="assunto",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="contato",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
