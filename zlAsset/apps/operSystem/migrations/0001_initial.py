# Generated by Django 2.1.5 on 2019-01-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=128, null=True)),
                ('os_type', models.CharField(blank=True, max_length=128, null=True)),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('sync', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=128, null=True)),
                ('host_ip', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('hdserver', models.CharField(blank=True, max_length=128, null=True)),
                ('department', models.CharField(blank=True, max_length=128, null=True)),
                ('team', models.CharField(blank=True, max_length=128, null=True)),
                ('use_member', models.CharField(blank=True, max_length=128, null=True)),
                ('start_date', models.CharField(blank=True, max_length=128, null=True)),
                ('end_date', models.CharField(blank=True, max_length=128, null=True)),
                ('run_env', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
