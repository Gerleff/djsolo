"""Users' related models"""
from django.db import models


class User(models.Model):
    """User's model"""
    name = models.CharField('Логин', max_length=220, null=True)
    user_id = models.IntegerField('Телеграм айди', primary_key=True)

    def __str__(self):
        return f'{self.user_id} ({self.name})'
    
    class Meta:
        """Meta-data"""
        db_table = 'users'


class Mailing(models.Model):
    """Mailing model"""
    content = models.TextField('Контент', null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    users = models.ManyToManyField(User, through='MailMessage')

    def __str__(self):
        return f' от {self.created_at}'

    class Meta:
        """Meta-data"""
        db_table = 'mailing'


class MailMessage(models.Model):
    """Mail message model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    message_id = models.IntegerField()

    def __str__(self):
        return (f'№{self.message_id} для {self.user.user_id}' 
                f' ({self.user.name}) от {self.mailing.created_at}')

    class Meta:
        """Meta-data"""
        db_table = 'mail_message'
