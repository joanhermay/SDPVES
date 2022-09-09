# Generated by Django 3.2.4 on 2021-06-16 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('vacunacion', '0006_alter_persona_municipio_de_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='municipio_de_nacimiento',
            field=models.ForeignKey(limit_choices_to={
                'id_departamento': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                     to='vacunacion.departamento', to_field='id_departamento')},
                                    on_delete=django.db.models.deletion.CASCADE, to='vacunacion.municipio'),
        ),
    ]
