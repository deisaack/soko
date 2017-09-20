from __future__ import unicode_literals


from authtools import forms as authtoolsforms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Field, Layout, Submit
class UserCreateForm(authtoolsforms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('email', placeholder="Enter Email", autofocus=""),
            Field('name', placeholder="Enter Full Name"),
            Submit('sign_up', 'Sign up', css_class="btn-warning"),
            )
