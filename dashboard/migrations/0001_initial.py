# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-02 13:06
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraphRules',
            fields=[
                ('graph_rule_id', models.AutoField(primary_key=True, serialize=False)),
                ('rule_name', models.CharField(max_length=1000, unique=True)),
                ('rule_packages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=1000), default=list, null=True, size=None)),
                ('rule_langs', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=400), default=list, null=True, size=None)),
                ('rule_relbranch', models.CharField(max_length=500, null=True)),
                ('created_on', models.DateTimeField(null=True)),
                ('rule_status', models.BooleanField()),
            ],
            options={
                'db_table': 'ts_graphrules',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('job_type', models.CharField(max_length=200)),
                ('job_start_time', models.DateTimeField()),
                ('job_end_time', models.DateTimeField(null=True)),
                ('job_log_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('job_result', models.NullBooleanField()),
                ('job_remarks', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'ts_jobs',
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('locale_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Locale ID')),
                ('lang_name', models.CharField(max_length=400, unique=True, verbose_name='Language Name')),
                ('locale_alias', models.CharField(max_length=50, null=True, verbose_name='Locale Alias')),
                ('lang_status', models.BooleanField(verbose_name='Enable/Disable')),
            ],
            options={
                'db_table': 'ts_locales',
            },
        ),
        migrations.CreateModel(
            name='LanguageSet',
            fields=[
                ('lang_set_id', models.AutoField(primary_key=True, serialize=False)),
                ('lang_set_name', models.CharField(max_length=1000, verbose_name='Language Set Name')),
                ('lang_set_slug', models.CharField(max_length=400, unique=True, verbose_name='Language Set SLUG')),
                ('lang_set_color', models.CharField(max_length=100, unique=True, verbose_name='Tag Colour')),
                ('locale_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, null=True, size=None, verbose_name='Locale IDs')),
            ],
            options={
                'db_table': 'ts_langset',
            },
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('package_id', models.AutoField(primary_key=True, serialize=False)),
                ('package_name', models.CharField(max_length=1000, unique=True)),
                ('upstream_name', models.CharField(max_length=1000, null=True)),
                ('upstream_url', models.URLField(max_length=2000, unique=True)),
                ('transplatform_name', models.CharField(max_length=1000, null=True)),
                ('transplatform_url', models.URLField(max_length=500)),
                ('release_streams', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=400), default=list, null=True, size=None)),
                ('package_details_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('details_json_lastupdated', models.DateTimeField(null=True)),
                ('package_name_mapping', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('release_branch_mapping', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('transtats_lastupdated', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'ts_packages',
            },
        ),
        migrations.CreateModel(
            name='ReleaseStream',
            fields=[
                ('relstream_id', models.AutoField(primary_key=True, serialize=False)),
                ('relstream_name', models.CharField(max_length=200, verbose_name='Release Stream Name')),
                ('relstream_slug', models.CharField(max_length=400, unique=True, verbose_name='Release Stream SLUG')),
                ('relstream_server', models.URLField(max_length=500, unique=True, verbose_name='Release Stream Server')),
                ('relstream_built', models.CharField(max_length=200, null=True, verbose_name='Release Build System')),
                ('srcpkg_format', models.CharField(max_length=50, null=True, verbose_name='Source Package Format')),
                ('top_url', models.URLField(max_length=500, unique=True, verbose_name='Top URL')),
                ('web_url', models.URLField(max_length=500, null=True, unique=True, verbose_name='Web URL')),
                ('krb_service', models.CharField(blank=True, max_length=200, null=True, verbose_name='Kerberos Service')),
                ('auth_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Auth Type')),
                ('amqp_server', models.CharField(blank=True, max_length=500, null=True, verbose_name='AMQP Server')),
                ('msgbus_exchange', models.CharField(blank=True, max_length=200, null=True, verbose_name='Message Bus Exchange')),
                ('major_milestones', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=1000), default=list, null=True, size=None, verbose_name='Major Milestones')),
                ('relstream_phases', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), default=list, null=True, size=None, verbose_name='Release Stream Phases')),
                ('relstream_status', models.BooleanField(verbose_name='Enable/Disable')),
            ],
            options={
                'db_table': 'ts_relstreams',
            },
        ),
        migrations.CreateModel(
            name='StreamBranches',
            fields=[
                ('relbranch_id', models.AutoField(primary_key=True, serialize=False)),
                ('relbranch_name', models.CharField(max_length=500)),
                ('relbranch_slug', models.CharField(max_length=500, unique=True)),
                ('relstream_slug', models.CharField(max_length=400)),
                ('lang_set', models.CharField(max_length=200)),
                ('scm_branch', models.CharField(max_length=100, null=True)),
                ('created_on', models.DateTimeField()),
                ('current_phase', models.CharField(max_length=200, null=True)),
                ('calendar_url', models.URLField(max_length=500, null=True)),
                ('schedule_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('sync_calendar', models.BooleanField(default=True)),
                ('notifications_flag', models.BooleanField(default=True)),
                ('track_trans_flag', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'ts_relbranches',
            },
        ),
        migrations.CreateModel(
            name='SyncStats',
            fields=[
                ('sync_id', models.AutoField(primary_key=True, serialize=False)),
                ('package_name', models.CharField(max_length=500)),
                ('job_uuid', models.UUIDField()),
                ('project_version', models.CharField(max_length=500, null=True)),
                ('stats_raw_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('sync_iter_count', models.IntegerField()),
                ('sync_visibility', models.BooleanField()),
            ],
            options={
                'db_table': 'ts_syncstats',
            },
        ),
        migrations.CreateModel(
            name='TransPlatform',
            fields=[
                ('platform_id', models.AutoField(primary_key=True, serialize=False)),
                ('engine_name', models.CharField(max_length=200, verbose_name='Platform Engine')),
                ('subject', models.CharField(max_length=200, null=True, verbose_name='Platform Subject')),
                ('api_url', models.URLField(max_length=500, unique=True, verbose_name='Server URL')),
                ('platform_slug', models.CharField(max_length=400, unique=True, verbose_name='Platform SLUG')),
                ('server_status', models.BooleanField(verbose_name='Enable/Disable')),
                ('projects_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('projects_lastupdated', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'ts_transplatforms',
            },
        ),
        migrations.AddField(
            model_name='packages',
            name='transplatform_slug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.TransPlatform', to_field='platform_slug'),
        ),
    ]
