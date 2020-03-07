# Generated by Django 2.0.7 on 2018-08-01 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DumpTruck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('nama', models.CharField(max_length=140)),
                ('merk', models.CharField(max_length=140)),
                ('unit_model', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Excavator',
            fields=[
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=140)),
                ('merk', models.CharField(max_length=140)),
                ('unit_model', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Lokasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('lokasi', models.CharField(max_length=140)),
                ('sublokasi', models.TextField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_inti', models.CharField(choices=[('COAL', 'COAL'), ('OB', 'OB')], default='COAL', max_length=140)),
                ('submaterial', models.CharField(blank=True, max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Muatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('shift', models.CharField(max_length=50)),
                ('shift_start_time', models.TimeField()),
                ('shift_end_time', models.TimeField()),
                ('ritasi', models.PositiveIntegerField()),
                ('bcm', models.PositiveIntegerField()),
                ('reported_problem', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
                ('tipe_pekerja', models.CharField(choices=[('OPERATOR', 'operator'), ('DRIVER', 'driver')], default='DRIVER', max_length=140)),
            ],
        ),
        migrations.AddField(
            model_name='muatan',
            name='driver_dumptruck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='muatan_driver_dumptruck', to='core.Worker'),
        ),
        migrations.AddField(
            model_name='muatan',
            name='dumpTruck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.DumpTruck'),
        ),
        migrations.AddField(
            model_name='muatan',
            name='excavator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Excavator'),
        ),
        migrations.AddField(
            model_name='muatan',
            name='lokasi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Lokasi'),
        ),
        migrations.AddField(
            model_name='muatan',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Material'),
        ),
        migrations.AddField(
            model_name='muatan',
            name='operator_excavator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='muatan_operator_excavator', to='core.Worker'),
        ),
        migrations.AddField(
            model_name='dumptruck',
            name='exacavator_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Excavator'),
        ),
    ]