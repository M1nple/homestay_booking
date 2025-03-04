from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # bảng User này là bảng có sẵn trong bộ xác thực của django bao gồm cả tk supperadmin khi tạo app
from django import forms

class RegisterUserForm(UserCreationForm): 
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 20, widget = forms.TextInput(attrs={'class': 'form-control'})) 
    last_name = forms.CharField(max_length = 20, )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# các trường có sẵn thì phải gọi như này class = 'form-control' boostrap 
    # def __init__(self, *args, **kwargs):
    #     super(RegisterUserForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'


    

