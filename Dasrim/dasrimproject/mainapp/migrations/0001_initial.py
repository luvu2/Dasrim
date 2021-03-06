# Generated by Django 3.1.2 on 2020-12-03 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('situation', models.CharField(max_length=100, null=True)),
                ('feel', models.CharField(max_length=100, null=True)),
                ('automatic', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('core_belief', models.CharField(max_length=100, null=True)),
                ('writer', models.CharField(max_length=100, null=True)),
                ('cognitive_error', models.CharField(max_length=100, null=True)),
                ('record_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyDiagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('summary', models.CharField(max_length=400, null=True)),
                ('self_image', models.CharField(max_length=20, null=True)),
                ('self_select', models.CharField(max_length=50, null=True)),
                ('feel', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('score1', models.IntegerField(null=True)),
                ('score2', models.IntegerField(null=True)),
                ('score3', models.IntegerField(null=True)),
                ('total_score', models.FloatField(null=True)),
                ('level', models.IntegerField(null=True)),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('nickname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=48)),
                ('gender', models.CharField(max_length=5)),
                ('age', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
