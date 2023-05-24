from django.db import models
from filer.fields.image import FilerImageField

from backend.users.models import Profile

RAM = ((0, '< 2GB'),
       (1, '2 GB'),
       (2, '4 GB'),
       (3, '6 GB'),
       (4, '8 GB'),
       (5, '10 GB'),
       (6, '12 GB'),
       (7, '14 GB'),
       (8, '16 GB'),)


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


class Categories(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    category_name = models.CharField('Название категории', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.category_name


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
    show_in_slider = models.BooleanField('Показывать на главной странице в слайдере', default=False, null=True,
                                         blank=True)
    new = models.BooleanField('Новинка', default=True, null=True, blank=True)
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

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)


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

    name = models.ForeignKey(Profile, verbose_name="Пользователь", on_delete=models.PROTECT)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )
    game = models.ForeignKey(Games, verbose_name="Игра", on_delete=models.CASCADE, related_name="reviews_set")

    def __str__(self):
        return f"{self.name} - {self.game}"


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    game = models.ForeignKey(to=Games, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.user} | Игра: {self.game.game_name}'

    def sum(self):
        return self.game.price_with_discount * self.quantity

    def de_json(self):
        basket_item = {
            'game_name': self.game.game_name,
            'quantity': self.quantity,
            'price_with_discount': float(self.game.price_with_discount),
            'sum': float(self.sum()),
        }
        return basket_item

    @classmethod
    def create_or_update(cls, game_id, user):
        baskets = Basket.objects.filter(user=user, game_id=game_id)

        if not baskets.exists():
            obj = Basket.objects.create(user=user, game_id=game_id, quantity=1)
            is_created = True
            return obj, is_created
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            is_crated = False
            return basket, is_crated


class Order(models.Model):
    basket_history = models.JSONField(default=dict)
    initiator = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    data_order = models.DateField('Дата заказа', auto_now_add=True, blank=True, null=True, editable=True)

    def __str__(self):
        return f'Order #{self.id}. {self.initiator.user}'
