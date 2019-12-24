# Generated by Django 3.0 on 2019-12-15 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminarea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('organizational_visibility', models.BooleanField(default=False)),
                ('global_visibility', models.BooleanField(default=False)),
                ('name', models.SlugField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminarea.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KeyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OAuth2Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('gitlab', 'Gitlab'), ('github', 'Github')], max_length=255)),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PublicKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ssh_public_key', models.TextField(max_length=2000)),
                ('fingerprint', models.CharField(max_length=512)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userarea.Device')),
            ],
            options={
                'permissions': (('can_assign_device', 'Can Assign Device to SShPublicKey'),),
                'unique_together': {('created_by', 'fingerprint')},
            },
        ),
        migrations.CreateModel(
            name='PublicKeyToKeyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('key_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userarea.KeyGroup')),
                ('public_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userarea.PublicKey')),
            ],
            options={
                'unique_together': {('public_key', 'key_group')},
            },
        ),
    ]