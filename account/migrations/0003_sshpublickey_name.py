# Generated by Django 2.2.7 on 2019-11-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_device_keygroup_oauth2account_sshpublickey_sshpublickeytokeygroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='sshpublickey',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
