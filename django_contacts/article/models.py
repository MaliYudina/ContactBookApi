from django.db import models


class Author(models.Model):
    name = models.CharField(verbose_name="Имя, Фамилия", max_length=255)
    email = models.EmailField(verbose_name="Email")
    id_db_author = models.AutoField(verbose_name="Индекс БД", primary_key=True, db_index=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=120)
    description = models.TextField(verbose_name="Краткое описание", max_length=120)
    CATEGORY_CHOICES = ((1, "Новости"),
                        (2, "Наука"),
                        (3, "Политика"),
                        (4, "Спорт"),
                        )
    category = models.IntegerField(verbose_name="Категория", choices=CATEGORY_CHOICES, default=2)
    body = models.TextField(verbose_name="Текст статьи")
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE,
                               verbose_name="Автор статьи")
    id_db_article = models.AutoField(primary_key=True, db_index=True, verbose_name="Индекс БД")

    def __str__(self):
        return self.title
