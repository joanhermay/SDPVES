# Generated by Django 3.2.4 on 2021-06-16 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacunacion', '0008_auto_20210616_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='codigo_departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacunacion.departamento', to_field='codigo_departamento'),
        ),
    ]
