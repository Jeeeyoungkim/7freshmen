from django import forms
from .models import User, Profile
from argon2 import PasswordHasher, exceptions

# 회원가입 폼
class SignupForm(forms.ModelForm):
    user_id = forms.CharField(
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-id',
                'placeholder' : '아이디'
            }
        ),
        error_messages={'required':'아이디를 입력해주세요.',
        'unique':'중복된 아이디입니다.'}
    )

    user_pw = forms.CharField(
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={'required':'비밀번호를 입력해주세요.'}
    )

    user_pw_confirm = forms.CharField(
        label='비밀번호 확인',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw-confirm',
                'placeholder' : '비밀번호 확인'
            }
        ),
        error_messages={'required':'비밀번호를 한번 더 입력해주세요.'}
    )

    user_name = forms.CharField(
        label='닉네임',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-name',
                'placeholder' : '닉네임'
            }
        ),
        error_messages={'required':'닉네임을 입력해주세요.',
        'unique':'중복된 닉네임입니다.'}
    )

    field_order = [
        'user_name',
        'user_id',
        'user_pw',
        'user_pw_confirm'
    ]

    class Meta:
        model = User
        fields = [
            'user_name','user_id','user_pw','user_pw_confirm'
        ]
    
    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id','')
        user_pw = cleaned_data.get('user_pw','')
        user_pw_confirm = cleaned_data.get('user_pw_confirm','')
        user_name = cleaned_data.get('user_name','')

        if user_pw != user_pw_confirm:
            return self.add_error('user_pw_confirm','비밀번호가 일치하지 않습니다.')
        else:
            self.user_id = user_id
            self.user_pw = PasswordHasher().hash(user_pw)
            self.user_pw_confirm = user_pw_confirm
            self.user_name = user_name

# 로그인 폼
class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length=32,
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-id',
                'placeholder' : '아이디'
            }
        ),
        error_messages={'required' : '아이디를 입력해주세요.'}
    )

    user_pw =  forms.CharField(
        max_length=128,
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요.'}
    )

    field_order = [
        'user_id',
        'user_pw',
    ]

    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id','')
        user_pw = cleaned_data.get('user_pw','')

        if user_id == '':
            return self.add_error('user_id','아이디를 다시 입력해주세요.')
        elif user_pw == '':
            return self.add_error('user_pw','비밀번호를 다시 입력해주세요.')
        else:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                return self.add_error('user_id','아이디가 존재하지 않습니다.')
            
            try:
                PasswordHasher().verify(user.user_pw,user_pw)
            except exceptions.VerifyMismatchError:
                return self.add_error('user_pw', '비밀번호가 일치하지 않습니다.')

# 프로필 폼
class ProfileForm(forms.ModelForm):
    school = forms.CharField(
        max_length=128,
        label='학교',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'school',
                'placeholder' : '학교'
            }
        ),
        error_messages={'required' : '학교를 입력해주세요.'}
    )

    major = forms.CharField(
        max_length=128,
        label='전공',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'major',
                'placeholder' : '전공'
            }
        ),
        error_messages={'required' : '전공/학부를 입력해주세요.'}
    )

    gender = forms.CharField(
        max_length=16,
        label='성별',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'gender',
                'placeholder' : '성별'
            }
        ),
        error_messages={'required' : '성별을 선택해주세요.'}
    )

    mbti = forms.CharField(
        max_length=16,
        label='MBTI',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'mbti',
                'placeholder' : 'MBTI'
            }
        ),
        error_messages={'required' : 'MBTI를 선택해주세요.'}
    )

    age = forms.IntegerField(
        label='age',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'age',
                'placeholder' : '성별'
            }
        ),
        error_messages={'required' : '나이를 입력해주세요.'}
    )

    field_order = [
        'school',
        'major',
        'gender',
        'mbti',
        'age'
    ]

    class Meta:
        model = Profile
        fields = [
            'school','major','gender','mbti','age'
        ]

    def clean(self):
        cleaned_data = super().clean()

        self.school = cleaned_data.get('school','')
        self.major = cleaned_data.get('major','')
        self.gender = cleaned_data.get('gender','')
        self.mbti = cleaned_data.get('mbti','')
        self.age = cleaned_data.get('age','')