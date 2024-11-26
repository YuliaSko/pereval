from django.db import models
from . import extensions


class User(models.Model):
    """
    Модель пользователя, тут хранится личная информация:
    эл. почта, ФИО, телефон
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    fam = models.CharField(max_length=50)
    oct = models.CharField(max_length=50, blank=True, default=None)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.email} {self.name} {self.fam} {self.oct} {self.phone}'


class Level(models.Model):
    """
    Модель для хранения категории сложности перевала
    """
    winter = models.CharField(max_length=2, choices=extensions.LEVEL_CHOICES)
    summer = models.CharField(max_length=2, choices=extensions.LEVEL_CHOICES)
    autumn = models.CharField(max_length=2, choices=extensions.LEVEL_CHOICES)
    spring = models.CharField(max_length=2, choices=extensions.LEVEL_CHOICES)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'


class Coord(models.Model):
    """
    Модель для хранения координат
    """
    latitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)
    height = models.IntegerField()

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'


class Pereval(models.Model):
    """
    Модель перевалов, тут хранится вся информация о перевале,
    связи с моделями координат, уровня сложности перевала и пользователем
    """
    beauty_title = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    other_titles = models.CharField(max_length=50)
    connect = models.CharField(max_length=250)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=extensions.STATUS)

    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    coord_id = models.ForeignKey(Coord, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} {self.beauty_title} {self.title}'


class PerevalImage(models.Model):
    """
    Модель для хранения изображений, есть связь с моделью Pereval
    """
    data = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.pk} {self.title} {self.pereval_id}'
