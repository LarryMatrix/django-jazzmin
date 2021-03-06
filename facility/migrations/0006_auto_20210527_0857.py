# Generated by Django 3.2.3 on 2021-05-27 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0005_alter_facility_closeddate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facility',
            old_name='Council',
            new_name='council',
        ),
        migrations.RenameField(
            model_name='facility',
            old_name='District',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='facility',
            old_name='Latitude',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='facility',
            old_name='Longitude',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='facility',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='facility',
            old_name='Region',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='facility',
            old_name='Village',
            new_name='village',
        ),
        migrations.RenameField(
            model_name='facility',
            old_name='Ward',
            new_name='ward',
        ),
        migrations.RenameField(
            model_name='facility',
            old_name='Zone',
            new_name='zone',
        ),
    ]
