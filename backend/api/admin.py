from api.models import (
    Favorite, Follow, Ingredient, IngredientRecipe, Recipe, ShoppingCart, Tag,
)
from django.contrib import admin


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit',
    )
    empty_value_display = '-empty-'
    list_filter = ('name',)
    

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_filter = ('author', 'name', 'tags')
    list_display = ('name', 'followers')

    @admin.display(empty_value=None)
    def followers(self, obj):
        return obj.favorited_by.all().count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    empty_value_display = '-empty-'


@admin.register(IngredientRecipe)
class IngredientRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'amount')
    empty_value_display = '-empty-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe_in_cart')
    empty_value_display = '-empty-'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    empty_value_display = '-empty-'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'favorite_recipe')
    empty_value_display = '-empty-'
