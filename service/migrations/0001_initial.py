# Generated by Django 4.2.3 on 2023-07-13 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='auto insertion', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='auto mification', verbose_name='Modified')),
                ('pic_height_field', models.PositiveSmallIntegerField(blank=True, editable=False, help_text="Size of Picture's height", null=True)),
                ('pic_width_field', models.PositiveSmallIntegerField(blank=True, editable=False, help_text="Size of Picture's width", null=True)),
                ('pic_alternate_text', models.CharField(help_text='Description about picture that is uploaded.', max_length=110)),
                ('banner_height_field', models.PositiveSmallIntegerField(blank=True, editable=False, help_text="Size of Picture's height", null=True)),
                ('banner_width_field', models.PositiveSmallIntegerField(blank=True, editable=False, help_text="Size of Picture's width", null=True)),
                ('banner_alternate_text', models.CharField(help_text='Description about picture that is uploaded.', max_length=110)),
                ('title', models.CharField(help_text='Service Name', max_length=100, unique=True, verbose_name='Title')),
                ('summary', models.CharField(help_text='Service summary', max_length=200, null=True, unique=True, verbose_name='Summary')),
                ('description', models.TextField(help_text='Description of Service', verbose_name='Description')),
                ('icon', models.CharField(help_text='Icon of service', max_length=50, unique=True, verbose_name='Icon')),
                ('picture', models.ImageField(height_field='pic_height_field', max_length=110, upload_to='service/', verbose_name='Picture', width_field='pic_width_field')),
                ('banner', models.ImageField(height_field='banner_height_field', max_length=110, upload_to='banner/', verbose_name='Banner', width_field='banner_width_field')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='auto insertion', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='auto mification', verbose_name='Modified')),
                ('title', models.CharField(help_text='Service Name', max_length=100, unique=True, verbose_name='Title')),
                ('attachment', models.FileField(upload_to='attachments/', verbose_name='Attachment')),
                ('service', models.ForeignKey(help_text='relation for many to one from service to attachment', on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='service.service')),
            ],
            options={
                'verbose_name': 'Service Attachment',
                'verbose_name_plural': 'Service Attachments',
            },
        ),
    ]
