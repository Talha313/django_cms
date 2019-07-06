from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'company_name', 'position_company', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['company_name'].label = "Company's Name"
        self.fields['position_company'].label = "Your position at the company"

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
