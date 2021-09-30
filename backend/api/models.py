from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MinValueValidator

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False,
                            verbose_name='Название ингридиента')
    measurement_unit = models.CharField(max_length=200, null=False,
                                        blank=False,
                                        verbose_name='Еденица измерения')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False,
                            blank=False, verbose_name='Тег')
    color = models.CharField(max_length=7, unique=True, null=False,
                             blank=False, verbose_name='Цвет')
    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Слаг')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта',
    )
    name = models.CharField(
        max_length=200, blank=False, null=False,
        verbose_name='Название рецепта',
    )
    image = models.ImageField(
        null=False, blank=False, 
        upload_to='recipes/', 
        verbose_name='Изображение блюда'
    )
    text = models.TextField(
        blank=False, null=False,
        verbose_name='Описание рецепта',
        help_text='Добавьте описание рецепта',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        verbose_name='Ингредиенты',
    )
    tags = models.ManyToManyField(
        Tag,
        blank=False,
        related_name='recipes',
        verbose_name='Теги',
    )
    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Время приготовления в минутах',
        help_text='Укажите время приготовления в минутах',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.PROTECT,
        verbose_name='Ингредиент, используемый в рецепте',
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='Рецепт'
    )
    amount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Количество ингредиента'
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'


class RecipeTags(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
                            verbose_name='Тег')

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return 'Тег рецепта'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorited_by',
        verbose_name='Рецепт',
    )

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'recipe'],
                       name='unique_recipe_in_user_favorite')]
        ordering = ('-id',)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='in_cart',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт в списке покупок',
    )

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'recipe'],
                       name='unique_recipe_in_user_shopping_list')]
        ordering = ('-id',)
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
