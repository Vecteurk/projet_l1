# Generated by Django 3.0.8 on 2021-06-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('postnom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=50)),
                ('sexe', models.CharField(max_length=2)),
            ],
        ),
    ]
