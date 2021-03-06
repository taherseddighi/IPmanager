# Generated by Django 2.2 on 2019-04-23 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Available_Public_IP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(max_length=255, null=True)),
                ('date_start', models.DateTimeField(blank=True)),
                ('date_expire', models.DateTimeField(blank=True)),
                ('price_bought', models.BigIntegerField(blank=True)),
                ('price_to_sell', models.BigIntegerField(blank=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Used_Private_IP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(max_length=255, null=True)),
                ('Device', models.CharField(max_length=255, null=True)),
                ('date_start', models.DateTimeField(blank=True)),
                ('date_expire', models.DateTimeField(blank=True)),
                ('price_bought', models.BigIntegerField(blank=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Used_Public_IP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(max_length=255, null=True)),
                ('client', models.CharField(blank=True, max_length=255, null=True)),
                ('date_start', models.DateTimeField(blank=True)),
                ('date_expire', models.DateTimeField(blank=True)),
                ('price_bought', models.BigIntegerField(blank=True)),
                ('price_sold', models.BigIntegerField(blank=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='ip_public_available',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ip_public_used',
            name='user',
        ),
        migrations.DeleteModel(
            name='IP_private_used',
        ),
        migrations.DeleteModel(
            name='IP_public_available',
        ),
        migrations.DeleteModel(
            name='IP_public_used',
        ),
    ]
