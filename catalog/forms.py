from django import forms
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version

exclude_text = "казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар"
exclude_words = set(exclude_text.split(", "))


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        words = set(cleaned_data.lower().split())
        if words.intersection(exclude_words):
            raise forms.ValidationError(f'Вы ввели одно из запрещенных слов: {exclude_words}.')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        words = set(cleaned_data.lower().split())
        if words.intersection(exclude_words):
            raise forms.ValidationError(f'Вы ввели одно из запрещенных слов: {exclude_words}.')
        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"


