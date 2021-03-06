# Generated by Django 2.1.5 on 2019-03-11 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_log_type', models.CharField(max_length=100)),
                ('Activity_log_details', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=100, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('id_number', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('driver_license_type', models.CharField(max_length=100)),
                ('driver_license_number', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='crew_pics')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('finance_type', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=100)),
                ('details', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=100, max_digits=100)),
                ('expense_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco.ExpenseType')),
            ],
        ),
        migrations.CreateModel(
            name='Matatu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reg_number', models.IntegerField()),
                ('reg_year', models.DateTimeField()),
                ('make_and_mode', models.CharField(max_length=100)),
                ('seats', models.IntegerField()),
                ('route', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='matatu_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('id_number', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='matatu',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco.Owner'),
        ),
        migrations.AddField(
            model_name='finance',
            name='matatu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco.Matatu'),
        ),
        migrations.AddField(
            model_name='crew',
            name='matatu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco.Matatu'),
        ),
        migrations.AddField(
            model_name='activity_log',
            name='matatu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco.Matatu'),
        ),
    ]
