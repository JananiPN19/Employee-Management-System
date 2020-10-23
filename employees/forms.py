from .models import Employee
from django.forms import ModelForm

class RegisterForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
class LoginForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('email_id','dob','job')