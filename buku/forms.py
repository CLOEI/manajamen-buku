from django import forms
from .models import Buku, Penulis, Penerbit, RakBuku, PenempatanBuku

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ['judul', 'penulis', 'tahun_terbit', 'penerbit', 'genre', 
                 'jumlah_halaman', 'sinopsis']
        widgets = {
            'sinopsis': forms.Textarea(attrs={'rows': 4}),
            'tahun_terbit': forms.NumberInput(attrs={'min': 1000, 'max': 2100}),
            'jumlah_halaman': forms.NumberInput(attrs={'min': 1}),
        }

class PenulisForm(forms.ModelForm):
    class Meta:
        model = Penulis
        fields = ['nama_depan', 'nama_belakang', 'tanggal_lahir', 'asal_negara']
        widgets = {
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date'}),
        }

class PenerbitForm(forms.ModelForm):
    class Meta:
        model = Penerbit
        fields = ['nama_penerbit', 'alamat', 'kota']

class RakBukuForm(forms.ModelForm):
    class Meta:
        model = RakBuku
        fields = ['nama_rak', 'lokasi_rak', 'kapasitas']
        widgets = {
            'kapasitas': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
        }
        help_texts = {
            'kapasitas': 'Jumlah maksimum buku yang dapat ditampung dalam rak ini',
        }

class PenempatanBukuForm(forms.ModelForm):
    class Meta:
        model = PenempatanBuku
        fields = ['rak']
        widgets = {
            'rak': forms.Select(attrs={'class': 'form-select'}),
        } 