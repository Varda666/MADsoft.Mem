from django.db import models


class Mem(models.Model):
    name = models.TextField(
        max_length=700, verbose_name='название'
    )
    text = models.TextField(verbose_name='текст')
    owner = models.ForeignKey(
        to='users.User', to_field='email',
        verbose_name='владелец мема', on_delete=models.DO_NOTHING
    )
    image = models.ImageField(upload_to='media/', verbose_name='изображение')

    class Meta:
        verbose_name = 'мем'
        verbose_name_plural = 'мемы'




