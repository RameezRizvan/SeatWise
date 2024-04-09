from django import forms

class signupform(forms.Form):
    firstname=forms.CharField(max_length=20)
    lastname=forms.CharField(max_length=20)
    email=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(max_length=20)
    confirmpass=forms.CharField(max_length=20)



class loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)



class cardform(forms.Form):
    image=forms.FileField()
    cardname=forms.CharField(max_length=20)
    genres=forms.CharField(max_length=50)
    category=forms.CharField(max_length=5)
    youtube = forms.CharField(max_length=50)
    language = forms.CharField(max_length=50)
    duration = forms.CharField(max_length=10)
    about = forms.CharField(max_length=500)



class seatselecform(forms.Form):
    date = forms.CharField(max_length=15)
    time = forms.CharField(max_length=15)
    selectedseats = forms.CharField(max_length=100)
    # user = forms.ForeignKey(signupmodel, on_delete=models.CASCADE)


