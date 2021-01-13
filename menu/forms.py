from django import forms
from restaurant.models import Category, Dish


class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': "Назва категорії", 'required': "required"}))
    category_order = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': "Порядок категорії у меню", 'required': "required"}))
    is_visible = forms.BooleanField(initial=True, required=False)

    class Meta(object):
        model = Category
        fields = ('title', 'category_order', 'is_visible')


class DishForm(forms.ModelForm):

    class Meta(object):
        model = Dish
        fields = ('title', 'price', 'photo', 'description', 'category')
