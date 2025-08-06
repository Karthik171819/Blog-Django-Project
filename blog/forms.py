
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from blog.models import Category, Post

#creating form for contact_page
class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Message', required=True)

#create a class or model for register_FORM
class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username',max_length=100, required=True)
    email = forms.CharField(label='Email', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True)
    password_confirm = forms.CharField(label='Confirm Password', max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

#custom validation for register form Non filed errors
    def clean(self):#clean() is inbuilt method
        cleaned_data = super().clean() #super class is ModelForm
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

#login_form
class LoginForm(forms.Form): #for field errors validation
    username = forms.CharField(label='username',max_length=100, required=True)
    password = forms.CharField(label='password',max_length=100, required=True)
    
    #handling login process
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid user and Password")

#forgot_password_form
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254, required=True)

    #checking the real-user e-mail_id are available in database
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No User Registered With This E-mail")
#ResetPasswordForm
class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(label='New Password', min_length=8)
    confirm_password = forms.CharField(label='Confirm Password', min_length=8)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password') #in this you should give that label name means label id=for
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Password do not match")

#creating a new_post form, whenever you create a Model Form create as well meta class also.
class PostForm(forms.ModelForm): #using ModelForm here because of posts are going to be add on in blog_post table when user newly created
    title = forms.CharField(label='Title', max_length=200, required=True)
    content = forms.CharField(label='Content', required=True)
    category = forms.ModelChoiceField(label='Category', required=True, queryset=Category.objects.all()) #its showing list of category_options

    class Meta:
        model = Post #its a type of model
        fields =['title', 'content', 'category'] #these fields are linked to Post table when we insert the data
    
    def clean(self):
        cleaned_data=super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        #custom validation for title and content about characters
        if title and len(title) < 5:
            raise forms.ValidationError('Title must be atleast 5 Characters long')
        
        if content and len(content) < 10:
            raise forms.ValidationError('Content must be atleast 10 characters long')