# Generated by Django 3.2.4 on 2021-06-16 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacunacion', '0003_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='municipio_de_nacimiento',
            field=models.ForeignKey(limit_choices_to={'id_departamento_id': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacunacion.departamento', to_field='id_departamento')}, on_delete=django.db.models.deletion.CASCADE, to='vacunacion.municipio'),
        ),
    ]
