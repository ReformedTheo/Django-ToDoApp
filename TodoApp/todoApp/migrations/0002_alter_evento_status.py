# Generated by Django 4.2.3 on 2023-07-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='status',
            field=models.CharField(choices=[('To do', 'TO DO'), ('in progress', 'IN PROGRESS'), ('Done', 'DONE')], max_length=50),
        ),
    ]
