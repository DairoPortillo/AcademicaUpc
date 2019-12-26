# Generated by Django 2.2.7 on 2019-12-26 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30, verbose_name='Nombre de categoría')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Linkage',
            fields=[
                ('linkage_id', models.AutoField(primary_key=True, serialize=False)),
                ('linkage_name', models.CharField(max_length=30, verbose_name='Nombre de vinculación')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['linkage_name'],
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('study_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('study_name', models.CharField(max_length=20)),
                ('study_percentage', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('teacher_dni', models.CharField(max_length=20, unique=True, verbose_name='Documento de identidad')),
                ('teacher_name', models.CharField(max_length=30, verbose_name='Primer nombre')),
                ('teacher_middle_name', models.CharField(blank=True, max_length=30, verbose_name='Segundo nombre')),
                ('teacher_last_name', models.CharField(max_length=30, verbose_name='Primer apellido')),
                ('teacher_middle_last_name', models.CharField(blank=True, max_length=30, verbose_name='Segundo apellido')),
                ('teacher_status', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('teacher_category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.Category')),
                ('teacher_linkage_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.Linkage')),
                ('teacher_study_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.Study')),
            ],
        ),
    ]
