from django.contrib import admin
from .models import Buku, Penulis, Penerbit, RakBuku, PenempatanBuku

class PenulisAdmin(admin.ModelAdmin):
    list_display = ('nama_depan', 'nama_belakang', 'asal_negara', 'tanggal_lahir')
    search_fields = ('nama_depan', 'nama_belakang', 'asal_negara')
    list_filter = ('asal_negara',)
    prepopulated_fields = {'slug': ('nama_depan', 'nama_belakang')}

class PenerbitAdmin(admin.ModelAdmin):
    list_display = ('nama_penerbit', 'kota', 'alamat')
    search_fields = ('nama_penerbit', 'kota')
    list_filter = ('kota',)
    prepopulated_fields = {'slug': ('nama_penerbit',)}

class RakBukuAdmin(admin.ModelAdmin):
    list_display = ('nama_rak', 'lokasi_rak')
    search_fields = ('nama_rak', 'lokasi_rak')
    list_filter = ('lokasi_rak',)
    prepopulated_fields = {'slug': ('nama_rak',)}

class PenempatanBukuInline(admin.TabularInline):
    model = PenempatanBuku
    extra = 1

class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul', 'penulis', 'penerbit', 'tahun_terbit', 'genre')
    list_filter = ('genre', 'tahun_terbit', 'penulis', 'penerbit')
    search_fields = ('judul', 'penulis__nama_depan', 'penulis__nama_belakang', 'penerbit__nama_penerbit')
    prepopulated_fields = {'slug': ('judul',)}
    inlines = [PenempatanBukuInline]
    date_hierarchy = 'tanggal_ditambahkan'

class PenempatanBukuAdmin(admin.ModelAdmin):
    list_display = ('buku', 'rak', 'tanggal_ditambahkan')
    list_filter = ('rak', 'tanggal_ditambahkan')
    search_fields = ('buku__judul', 'rak__nama_rak')
    date_hierarchy = 'tanggal_ditambahkan'

admin.site.register(Penulis, PenulisAdmin)
admin.site.register(Penerbit, PenerbitAdmin)
admin.site.register(RakBuku, RakBukuAdmin)
admin.site.register(Buku, BukuAdmin)
admin.site.register(PenempatanBuku, PenempatanBukuAdmin)
