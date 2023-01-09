from django import forms
from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image', 'is_hidden')

    def text_attr(self, field):
        field.widget.attrs.update({
            'class': 'form-control',
            "name": "user_activity",
            "placeholder": "Share what you've been up to..."
        })

    def image_attr(self, field):
        field.widget.attrs.update({
            'class': 'form-control'
        })

    def is_hidden_attr(self, field):
        field.widget.attrs.update({
            'class': 'form-check-input'
        })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            method = getattr(self, f'{field_name}_attr', None)
            if method:
                method(field)
