from pyexpat import model
from django.forms import ModelForm
from .models import Room, User

from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.layout import Submit, Layout, Div, Fieldset

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import UserCreationForm


class RoomForm(ModelForm):
    
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-roomForm'
        self.helper.form_class = 'roomForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'room_submit'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        self.helper.layout = Layout(
            Fieldset('SOMETHING',
                    Field('host', placeholder='Select a Host'),
                    Div('topic', title='Select One'),
            ),
            Fieldset('MORETHING', 'name', 'description', style="color: brown;"
            ),
        )

class UserForm(ModelForm):
    class Meta:
        model = User
        fields= ['username', 'email', 'name', 'bio', 'avatar']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['name', 'username', 'email', 'password1', 'password2']