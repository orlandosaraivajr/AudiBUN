from django import forms


class EmpresaForm(forms.Form):
    ref_cad = forms.CharField(label='Referência Cadastral',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Nome da Empresa',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    atividade = forms.CharField(label='Atividade',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco = forms.CharField(label='Endereço',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    quadra = forms.CharField(label='Quadra',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    lote = forms.CharField(label='Lote',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Telefone',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    responsavel = forms.CharField(label='Responsável',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    situacao = forms.CharField(label='Situação',
        widget=forms.TextInput(attrs={'class': 'form-control'}))