# Generated by Django 3.1.2 on 2020-11-02 06:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import interface.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartype', models.CharField(max_length=200, null=True)),
                ('carnum', models.CharField(max_length=200, null=True)),
                ('stack_drive', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OperationLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(null=True)),
                ('datetimes', models.DateTimeField(default=datetime.datetime(2020, 11, 2, 6, 14, 36, 599447, tzinfo=utc))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('distance', models.IntegerField(default=0)),
                ('passenger', models.IntegerField(default=0)),
                ('isoweeks', models.IntegerField(default=1)),
                ('cardata', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='operation', related_query_name='cardata', to='interface.cardatamodel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_pos', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('files', models.FileField(null=True, upload_to=interface.models.upload_path)),
                ('filename', models.CharField(max_length=50, null=True)),
                ('filetype', models.CharField(max_length=10, null=True)),
                ('fileviewsize', models.CharField(max_length=10, null=True)),
                ('filesize', models.IntegerField(null=True)),
                ('oplog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files_to_oplog', related_query_name='oplog_to_file', to='interface.operationlogmodel')),
            ],
        ),
        migrations.CreateModel(
            name='DTGDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('datetimes', models.DateTimeField()),
                ('daily_drive', models.IntegerField()),
                ('stack_drive', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('rpm', models.IntegerField()),
                ('brake_signal', models.IntegerField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('position_angle', models.IntegerField()),
                ('acc_x', models.FloatField()),
                ('acc_y', models.FloatField()),
                ('device_status', models.IntegerField()),
                ('dtgfile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dtgdatas_to_dtgfiles', related_query_name='dtgfile_to_dtgdata', to='interface.filemodel')),
                ('oplog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dtgdatas_to_oplog', related_query_name='oplog_to_dtgdata', to='interface.operationlogmodel')),
            ],
        ),
    ]
