# Generated by Django 2.2.7 on 2019-11-16 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publish', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToPublishGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usertopublish_creator', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('publish_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publish.PublishGroup')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SSHPrivateKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssh_private_key', models.TextField(max_length=2000)),
                ('fingerprint', models.CharField(max_length=512)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_assign_device', 'Can Assign Device to SShPublicKey'),),
                'unique_together': {('created_by', 'fingerprint')},
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('ssh_private_key', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='publish.SSHPrivateKey')),
            ],
        ),
    ]