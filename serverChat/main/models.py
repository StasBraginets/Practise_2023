# -*- coding: utf-8 -*-
from django.db import models

# Описуємо таблицю-об'єкт
class Users(models.Model):
    # Назва поля
    nickname = models.CharField('Nickname', max_length=25)
    password = models.CharField('Password', max_length=15)

    def __str__(self):
        return str(self.nickname)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
