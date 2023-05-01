from django.db import models

LANGUAGE = ((1, 'Русский'),
            (2, 'Английский'),
            (0, 'Польский'),
            (3, 'Румынский'))


class Games(models.Model):
    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'

    nazvanie = models.CharField('Название игры', max_length=255, blank=True, null=True)
    upload_date = models.DateTimeField('Дата загрузки торрента', auto_now_add=True, editable=False, null=True)
    main_image = models.ImageField('Обложка игры', upload_to='images/', null=True, blank=True)
    release_date = models.DateTimeField('Дата выпуска', auto_now_add=True, editable=True)
    developer = models.CharField('Разработчик', max_length=255, blank=True, null=True)
    interface_language = models.IntegerField('Язык интерфейса', choices=LANGUAGE, null=True, blank=True)
    description = models.TextField('Описание игры', null=True, blank=True)

    os = models.CharField('Операционная система', max_length=255, blank=True, null=True)
    processor = models.CharField('Процессор', max_length=255, blank=True, null=True)
    ram = models.CharField('Оперативная память', max_length=255, blank=True, null=True)
    video_card = models.CharField('Видеокарта', max_length=255, blank=True, null=True)
    free_memory = models.CharField('Место на жестком диске', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nazvanie
