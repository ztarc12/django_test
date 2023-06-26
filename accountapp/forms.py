from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    # 아래 구문은 아이디 form을 disabled 해주는  코드
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True

    # 아래 구문은 disabled 된 form의 기능을 건너 뛰는 코드
    def clean_username(self):
        return self.cleaned_data['username']
