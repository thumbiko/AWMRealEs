# Generated by Django 5.1.4 on 2025-01-02 15:55

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('type', models.CharField(choices=[('University', 'University'), ('Hospital', 'Hospital'), ('Stadium', 'Stadium')], max_length=50)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='CCTV',
            new_name='cctv',
        ),
        migrations.AddField(
            model_name='listing',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='picture5',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(blank=True, choices=[('Inner London', 'Inner London'), ('Outer London', 'Outer London')], max_length=20, null=True),
        ),
    ]
