# Generated by Django 4.0.2 on 2022-02-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField(max_length=125, verbose_name='Tanıtıcı Paragraf')),
                ('group1_title', models.CharField(max_length=10, verbose_name='Link Grubu 1 Başlık')),
                ('g1_link1_name', models.CharField(max_length=30, verbose_name='Group 1 Link-1 Ad')),
                ('g1_link1', models.URLField(verbose_name='Group 1 Link-1 Url')),
                ('g1_link2_name', models.CharField(max_length=30, verbose_name='Group 1 Link-2 Ad')),
                ('g1_link2', models.URLField(verbose_name='Group 1 Link-2 Url')),
                ('g1_link3_name', models.CharField(max_length=30, verbose_name='Group 1 Link-3 Ad')),
                ('g1_link3', models.URLField(verbose_name='Group 1 Link-3 Url')),
                ('g1_link4_name', models.CharField(max_length=30, verbose_name='Group 1 Link-2 Ad')),
                ('g1_link4', models.URLField(verbose_name='Group 1 Link-4 Url')),
                ('group2_title', models.CharField(max_length=10, verbose_name='Link Grubu 2 Başlık')),
                ('g2_link1_name', models.CharField(max_length=30, verbose_name='Group 2 Link-1 Ad')),
                ('g2_link1', models.URLField(verbose_name='Group 2 Link-1 Url')),
                ('g2_link2_name', models.CharField(max_length=30, verbose_name='Group 2 Link-2 Ad')),
                ('g2_link2', models.URLField(verbose_name='Group 2 Link-2 Url')),
                ('g2_link3_name', models.CharField(max_length=30, verbose_name='Group 2 Link-3 Ad')),
                ('g2_link3', models.URLField(verbose_name='Group 2 Link-3 Url')),
                ('g2_link4_name', models.CharField(max_length=30, verbose_name='Group 2 Link-4 Ad')),
                ('g2_link4', models.URLField(verbose_name='Group 2 Link-4 Url')),
                ('adress', models.CharField(max_length=25, verbose_name='Adres')),
                ('mail', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('phone', models.CharField(max_length=16, verbose_name='Telefon')),
                ('whatsapp', models.CharField(max_length=16, verbose_name='Whatsapp')),
                ('edited_date', models.DateTimeField(auto_now=True, verbose_name='Düzenleme Tarihi')),
                ('social_link1', models.URLField(verbose_name='Sosyal Medya 1 Url')),
                ('social_link1_icon', models.CharField(max_length=50, verbose_name='Sosyal Medya İkon 1 ')),
                ('social_link2', models.URLField(verbose_name='Sosyal Medya 2 Url')),
                ('social_link2_icon', models.CharField(max_length=50, verbose_name='Sosyal Medya İkon 2 ')),
                ('social_link3', models.URLField(verbose_name='Sosyal Medya 3 Url')),
                ('social_link3_icon', models.CharField(max_length=50, verbose_name='Sosyal Medya İkon 3 ')),
                ('social_link4', models.URLField(verbose_name='Sosyal Medya 4 Url')),
                ('social_link4_icon', models.CharField(max_length=50, verbose_name='Sosyal Medya İkon 4')),
            ],
        ),
    ]
