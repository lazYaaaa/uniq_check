from django import forms
from main.models import SiteComment, SiteRating


class SiteCommentCreate(forms.ModelForm):
    content = forms.TextInput()

    class Meta:
        model = SiteComment
        fields = ['content']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = ''
        self.fields['content'].widget.attrs.update(placeholder='Написать комментарий...')


class SiteSearchForm(forms.Form):
    keywords = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['keywords'].label = ''
        self.fields['keywords'].widget.attrs.update(placeholder='С каким сайтом у вас возникли проблемы?')
        self.fields['keywords'].widget.attrs.update({'class': 'w-full p-3'})


class RatingForm(forms.ModelForm):
    rating = forms.IntegerField(required=False)

    class Meta:
        model = SiteRating
        fields = ['rating']


class GraphImageForm(forms.Form):
    graph = forms.CharField(required=False)
    graph.widget = graph.hidden_widget()
