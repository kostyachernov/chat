from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', verbose_name='Отправитель')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver', verbose_name='Получатель')
    message = models.CharField(max_length=1200, verbose_name='Сообщение')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    is_read = models.BooleanField(default=False, verbose_name='Статус')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'
        ordering = ('timestamp',)


