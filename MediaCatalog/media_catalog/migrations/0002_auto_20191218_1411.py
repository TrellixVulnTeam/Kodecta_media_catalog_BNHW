# Generated by Django 3.0 on 2019-12-18 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.AlterModelOptions(
            name='creator',
            options={'verbose_name': 'Creator', 'verbose_name_plural': 'Creators'},
        ),
        migrations.CreateModel(
            name='MediaPublish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_expiry', models.DateTimeField(verbose_name='Date of expiry for media')),
                ('meida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_catalog.Media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_catalog.User')),
            ],
        ),
    ]
