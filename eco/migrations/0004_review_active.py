# Generated by Django 2.2.3 on 2019-08-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco', '0003_remove_review_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]