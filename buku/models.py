from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Penulis(models.Model):
    nama_depan = models.CharField(max_length=100)
    nama_belakang = models.CharField(max_length=100)
    tanggal_lahir = models.DateField(null=True, blank=True)
    asal_negara = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Penulis"
        ordering = ['nama_belakang', 'nama_depan']

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.nama_depan}-{self.nama_belakang}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('penulis-detail', kwargs={'slug': self.slug})

class Penerbit(models.Model):
    nama_penerbit = models.CharField(max_length=200)
    alamat = models.CharField(max_length=200, null=True, blank=True)
    kota = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Penerbit"
        ordering = ['nama_penerbit']

    def __str__(self):
        return self.nama_penerbit

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama_penerbit)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('penerbit-detail', kwargs={'slug': self.slug})

class RakBuku(models.Model):
    nama_rak = models.CharField(max_length=100)
    lokasi_rak = models.CharField(max_length=200)
    kapasitas = models.PositiveIntegerField(default=100, help_text="Jumlah maksimum buku yang dapat ditampung")
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Rak Buku"
        ordering = ['nama_rak']

    def __str__(self):
        return f"{self.nama_rak} ({self.lokasi_rak})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama_rak)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('rak-detail', kwargs={'slug': self.slug})

    @property
    def jumlah_buku(self):
        """Returns the current number of books in this shelf"""
        return self.buku.count()

    @property
    def sisa_kapasitas(self):
        """Returns the remaining capacity of this shelf"""
        return self.kapasitas - self.jumlah_buku

class Buku(models.Model):
    GENRE_CHOICES = [
        ('FIKSI', 'Fiksi'),
        ('NONFIKSI', 'Non-Fiksi'),
        ('SASTRA', 'Sastra'),
        ('SEJARAH', 'Sejarah'),
        ('SAINS', 'Sains'),
        ('TEKNOLOGI', 'Teknologi'),
        ('BISNIS', 'Bisnis'),
        ('LAINNYA', 'Lainnya'),
    ]

    judul = models.CharField(max_length=200)
    penulis = models.ForeignKey(Penulis, on_delete=models.CASCADE, related_name='buku')
    tahun_terbit = models.IntegerField()
    penerbit = models.ForeignKey(Penerbit, on_delete=models.CASCADE, related_name='buku')
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, null=True, blank=True)
    jumlah_halaman = models.IntegerField(null=True, blank=True)
    sinopsis = models.TextField(null=True, blank=True)
    rak = models.ManyToManyField(RakBuku, through='PenempatanBuku', related_name='buku')
    slug = models.SlugField(unique=True, blank=True)
    tanggal_ditambahkan = models.DateTimeField(auto_now_add=True)
    tanggal_diupdate = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Buku"
        ordering = ['judul']

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('buku-detail', kwargs={'slug': self.slug})

class PenempatanBuku(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    rak = models.ForeignKey(RakBuku, on_delete=models.CASCADE, related_name='penempatan')
    tanggal_ditambahkan = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Penempatan Buku"
        unique_together = ['buku', 'rak']
        ordering = ['-tanggal_ditambahkan']

    def __str__(self):
        return f"{self.buku.judul} di {self.rak.nama_rak}"
