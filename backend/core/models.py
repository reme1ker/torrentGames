from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

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


class InterfaceLanguage(models.Model):
    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    language_name = models.CharField('Язык', max_length=255, blank=False, null=False)

    def __str__(self):
        return self.language_name


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

    game_name = models.CharField('Название игры', max_length=255, blank=False, null=False)
    price = models.IntegerField('Цена игры', null=True, blank=True)
    discount = models.IntegerField('Скидка на игру в процентах', null=True, blank=True)
    price_with_discount = models.IntegerField('Цена игры со скидкой', null=True, blank=True)
    main_image = models.ImageField('Обложка игры', upload_to='images/', null=False, blank=False)
    release_date = models.DateField('Дата выпуска', auto_now_add=False, editable=True)
    developer = models.ForeignKey(Developers, verbose_name='Разработчик', on_delete=models.PROTECT, blank=True,
                                  null=True)
    interface_language = models.ForeignKey(InterfaceLanguage, on_delete=models.PROTECT, verbose_name='Язык интерфейса',
                                           null=True, blank=True)
    description = models.TextField('Описание игры', null=True, blank=True)
    categories = models.ManyToManyField(Categories, verbose_name='Категория')
    os = models.ForeignKey(OperationSystems, verbose_name='Операционная система', on_delete=models.PROTECT, blank=True,
                           null=True)
    processor = models.ForeignKey(Processors, verbose_name='Процессор', on_delete=models.PROTECT, blank=True, null=True)
    ram = models.IntegerField('Оперативная память', choices=RAM, null=True, blank=True)
    video_card = models.ForeignKey(VideoCards, verbose_name='Видеокарта', on_delete=models.PROTECT, blank=True,
                                   null=True)
    free_memory = models.CharField('Место на жестком диске', max_length=255, blank=True, null=True)
    trailer = models.CharField('Трейлер игры (ссылка iframe youtube)', max_length=1000, blank=True, null=True)
    score = models.IntegerField('Популярность игры', null=True, blank=True, editable=False)

    def __str__(self):
        return self.game_name

    def get_categories(self):
        return ", ".join([str(p) for p in self.categories.all()])

    def price_with_discount(self):
        if self.discount:
            self.price_with_discount = int(self.price - ((self.price / 100) * self.discount))
            return self.price_with_discount
        else:
            return self.price_with_discount

    def get_foto_set(self):
        return self.foto_set.select_related('img')


class Screenchots(models.Model):
    class Meta:
        verbose_name = 'Cкриншот'
        verbose_name_plural = 'Cкриншоты'

    games = models.ForeignKey(Games, verbose_name='Игры', on_delete=models.CASCADE, null=True,
                              blank=True,
                              related_name='foto_set')
    img = FilerImageField(verbose_name='Фото', on_delete=models.CASCADE, )


class Review(models.Model):
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    """Отзывы"""
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )
    movie = models.ForeignKey(Games, verbose_name="Игра", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.name} - {self.movie}"
