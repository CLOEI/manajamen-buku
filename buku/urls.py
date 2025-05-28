from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Buku URLs
    path('buku/', views.BukuListView.as_view(), name='buku-list'),
    path('buku/tambah/', views.BukuCreateView.as_view(), name='buku-create'),
    path('buku/<slug:slug>/', views.BukuDetailView.as_view(), name='buku-detail'),
    path('buku/<slug:slug>/edit/', views.BukuUpdateView.as_view(), name='buku-update'),
    path('buku/<slug:slug>/hapus/', views.BukuDeleteView.as_view(), name='buku-delete'),
    path('buku/<int:buku_id>/tambah-penempatan/', views.tambah_penempatan, name='tambah-penempatan'),
    path('penempatan/<int:penempatan_id>/hapus/', views.hapus_penempatan, name='hapus-penempatan'),

    # Penulis URLs
    path('penulis/', views.PenulisListView.as_view(), name='penulis-list'),
    path('penulis/tambah/', views.PenulisCreateView.as_view(), name='penulis-create'),
    path('penulis/<slug:slug>/', views.PenulisDetailView.as_view(), name='penulis-detail'),
    path('penulis/<slug:slug>/edit/', views.PenulisUpdateView.as_view(), name='penulis-update'),
    path('penulis/<slug:slug>/hapus/', views.PenulisDeleteView.as_view(), name='penulis-delete'),

    # Penerbit URLs
    path('penerbit/', views.PenerbitListView.as_view(), name='penerbit-list'),
    path('penerbit/tambah/', views.PenerbitCreateView.as_view(), name='penerbit-create'),
    path('penerbit/<slug:slug>/', views.PenerbitDetailView.as_view(), name='penerbit-detail'),
    path('penerbit/<slug:slug>/edit/', views.PenerbitUpdateView.as_view(), name='penerbit-update'),
    path('penerbit/<slug:slug>/hapus/', views.PenerbitDeleteView.as_view(), name='penerbit-delete'),

    # Rak Buku URLs
    path('rak/', views.RakBukuListView.as_view(), name='rak-list'),
    path('rak/tambah/', views.RakBukuCreateView.as_view(), name='rak-create'),
    path('rak/<slug:slug>/', views.RakBukuDetailView.as_view(), name='rak-detail'),
    path('rak/<slug:slug>/update/', views.RakBukuUpdateView.as_view(), name='rak-update'),
    path('rak/<slug:slug>/delete/', views.RakBukuDeleteView.as_view(), name='rak-delete'),
    path('rak/<slug:rak_slug>/tambah-buku/', views.PenempatanBukuCreateView.as_view(), name='penempatan-create'),
    path('penempatan/<int:pk>/delete/', views.PenempatanBukuDeleteView.as_view(), name='penempatan-delete'),
] 