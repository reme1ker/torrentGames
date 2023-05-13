from django.db import models

LANGUAGE = ((1, 'Русский'),
            (2, 'Английский'),
            (0, 'Польский'),
            (3, 'Румынский'))

RAM = ((0, '< 2GB'),
       (1, '2 GB'),
       (2, '4 GB'),
       (3, '6 GB'),
       (4, '8 GB'),
       (5, '10 GB'),
       (6, '12 GB'),
       (7, '14 GB'),
       (8, '16 GB'),)


class Categories(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    category_name = models.CharField('Название категории', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.category_name


class Developers(models.Model):
    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'

    developer_name = models.CharField('Название компании', max_length=255, blank=False, null=False)

    def __str__(self):
        return self.developer_name


class OperationSystems(models.Model):
    class Meta:
        verbose_name = 'Операционная система'
        verbose_name_plural = 'Операционные системы'

    os_name = models.CharField('Операционная система', max_length=255, blank=False, null=False)

    def __str__(self):
        return self.os_name


class Processors(models.Model):
    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'

    processor_name = models.CharField('Процессор', max_length=255, blank=False, null=False)

    def __str__(self):
        return self.processor_name


class VideoCards(models.Model):
    class Meta:
        verbose_name = 'Видеокарта'
        verbose_name_plural = 'Видеокарты'

    video_card_name = models.CharField('Видеокарта', max_length=255, blank=False, null=False)

    def __str__(self):
        return self.video_card_name


class Games(models.Model):
    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'

    game_name = models.CharField('Название игры', max_length=255, blank=True, null=True)
    upload_date = models.DateTimeField('Дата загрузки торрента', auto_now_add=True, editable=False, null=True)
    main_image = models.ImageField('Обложка игры', upload_to='images/', null=True, blank=True)
    release_date = models.DateTimeField('Дата выпуска', auto_now_add=True, editable=True)
    developer = models.ForeignKey(Developers, verbose_name='Разработчик', on_delete=models.PROTECT, blank=True,
                                  null=True)
    interface_language = models.IntegerField('Язык интерфейса', choices=LANGUAGE, null=True, blank=True)
    description = models.TextField('Описание игры', null=True, blank=True)
    categories = models.ManyToManyField(Categories, verbose_name='Категория')
    os = models.ForeignKey(OperationSystems, verbose_name='Операционная система', on_delete=models.PROTECT, blank=True,
                           null=True)
    processor = models.ForeignKey(Processors, verbose_name='Процессор', on_delete=models.PROTECT, blank=True, null=True)
    ram = models.IntegerField('Оперативная память', choices=RAM, null=True, blank=True)
    video_card = models.ForeignKey(VideoCards, verbose_name='Видеокарта', on_delete=models.PROTECT, blank=True,
                                   null=True)
    free_memory = models.CharField('Место на жестком диске', max_length=255, blank=True, null=True)
    download_counter = models.IntegerField('Количество скачиваний', null=True, blank=True, editable=False)
    score = models.IntegerField('Оценка пользователей', null=True, blank=True, editable=False)

    def __str__(self):
        return self.game_name

    def get_categories(self):
        return ", ".join([str(p) for p in self.categories.all()])
