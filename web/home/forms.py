from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre', 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'w-[100%] rounded-full'})
    )
    email = forms.EmailField(
        label='Correo',
        widget=forms.EmailInput(attrs={'placeholder': 'Correo', 'class': 'w-[100%] rounded-full'})
    )
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'placeholder': 'Mensaje', 'class': 'w-[100%] rounded-xl'})
    )