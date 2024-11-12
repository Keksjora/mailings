# Generated by Django 5.1.3 on 2024-11-09 12:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MailingRecipient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("full_name", models.CharField(max_length=150, verbose_name="Ф.И.О")),
                ("comment", models.TextField()),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "Получатель",
                "verbose_name_plural": "Получатели",
                "ordering": ["full_name", "email"],
                "permissions": [
                    ("can_view_all_mailingrecipient", "can view all mailingrecipient")
                ],
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject",
                    models.CharField(max_length=250, verbose_name="тема письма"),
                ),
                ("body_of_the_letter", models.TextField(verbose_name="Сообщение")),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщений",
                "ordering": ["subject"],
                "permissions": [("can_view_all_messages", "can view all messages")],
            },
        ),
        migrations.CreateModel(
            name="Newsletter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sent_date", models.DateTimeField(auto_now_add=True)),
                ("end_of_sending", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("завершена", "завершена"),
                            ("создана", "создана"),
                            ("запущена", "запущена"),
                        ],
                        default="создана",
                        max_length=50,
                    ),
                ),
                ("is_blocked", models.BooleanField(default=False)),
                (
                    "message",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="newapp.message"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец",
                    ),
                ),
                (
                    "recipients",
                    models.ManyToManyField(
                        to="newapp.mailingrecipient", verbose_name="Получатели"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статус",
                "verbose_name_plural": "Статусы",
                "ordering": ["status", "sent_date", "end_of_sending"],
                "permissions": [
                    ("can_view_all_mailings", "can view all mailings"),
                    ("can_disable_mailings", "can disable mailings"),
                ],
            },
        ),
        migrations.CreateModel(
            name="MailingAttempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_and_time_of_attempt", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("успешно", "успешно"), ("не успешно", "не успешно")],
                        max_length=50,
                    ),
                ),
                ("mail_server_response", models.TextField(blank=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "recipients",
                    models.ManyToManyField(blank=True, to="newapp.mailingrecipient"),
                ),
                (
                    "newsletter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attempts",
                        to="newapp.newsletter",
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка",
                "verbose_name_plural": "Попытки",
                "ordering": ["status", "date_and_time_of_attempt"],
                "permissions": [
                    ("can_view_all_mailings_attempts", "can view all mailings attempts")
                ],
            },
        ),
        migrations.CreateModel(
            name="UserMailingStatistics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_mailings", models.IntegerField(default=0)),
                ("successful_mailings", models.IntegerField(default=0)),
                ("failed_mailings", models.IntegerField(default=0)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]