# Generated by Django 2.2.7 on 2019-12-12 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
