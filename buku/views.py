from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from .models import Buku, Penulis, Penerbit, RakBuku, PenempatanBuku
from .forms import BukuForm, PenulisForm, PenerbitForm, RakBukuForm, PenempatanBukuForm

# Home View
def home(request):
    total_buku = Buku.objects.count()
    total_penulis = Penulis.objects.count()
    total_penerbit = Penerbit.objects.count()
    total_rak = RakBuku.objects.count()
    buku_terbaru = Buku.objects.order_by('-tanggal_ditambahkan')[:5]
    
    context = {
        'total_buku': total_buku,
        'total_penulis': total_penulis,
        'total_penerbit': total_penerbit,
        'total_rak': total_rak,
        'buku_terbaru': buku_terbaru,
    }
    return render(request, 'buku/home.html', context)

# Buku Views
class BukuListView(ListView):
    model = Buku
    template_name = 'buku/buku_list.html'
    context_object_name = 'buku_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(judul__icontains=search_query) |
                Q(penulis__nama_depan__icontains=search_query) |
                Q(penulis__nama_belakang__icontains=search_query) |
                Q(penerbit__nama_penerbit__icontains=search_query)
            ).distinct()
        return queryset

class BukuDetailView(DetailView):
    model = Buku
    template_name = 'buku/buku_detail.html'
    context_object_name = 'buku'

class BukuCreateView(LoginRequiredMixin, CreateView):
    model = Buku
    form_class = BukuForm
    template_name = 'buku/buku_form.html'
    success_url = reverse_lazy('buku-list')

    def form_valid(self, form):
        messages.success(self.request, 'Buku berhasil ditambahkan!')
        return super().form_valid(form)

class BukuUpdateView(LoginRequiredMixin, UpdateView):
    model = Buku
    form_class = BukuForm
    template_name = 'buku/buku_form.html'
    success_url = reverse_lazy('buku-list')

    def form_valid(self, form):
        messages.success(self.request, 'Buku berhasil diperbarui!')
        return super().form_valid(form)

class BukuDeleteView(LoginRequiredMixin, DeleteView):
    model = Buku
    template_name = 'buku/buku_confirm_delete.html'
    success_url = reverse_lazy('buku-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Buku berhasil dihapus!')
        return super().delete(request, *args, **kwargs)

# Penulis Views
class PenulisListView(ListView):
    model = Penulis
    template_name = 'buku/penulis_list.html'
    context_object_name = 'penulis_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nama_depan__icontains=search_query) |
                Q(nama_belakang__icontains=search_query)
            )
        return queryset

class PenulisDetailView(DetailView):
    model = Penulis
    template_name = 'buku/penulis_detail.html'
    context_object_name = 'penulis'

class PenulisCreateView(LoginRequiredMixin, CreateView):
    model = Penulis
    form_class = PenulisForm
    template_name = 'buku/penulis_form.html'
    success_url = reverse_lazy('penulis-list')

    def form_valid(self, form):
        messages.success(self.request, 'Penulis berhasil ditambahkan!')
        return super().form_valid(form)

class PenulisUpdateView(LoginRequiredMixin, UpdateView):
    model = Penulis
    form_class = PenulisForm
    template_name = 'buku/penulis_form.html'
    success_url = reverse_lazy('penulis-list')

    def form_valid(self, form):
        messages.success(self.request, 'Penulis berhasil diperbarui!')
        return super().form_valid(form)

class PenulisDeleteView(LoginRequiredMixin, DeleteView):
    model = Penulis
    template_name = 'buku/penulis_confirm_delete.html'
    success_url = reverse_lazy('penulis-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Penulis berhasil dihapus!')
        return super().delete(request, *args, **kwargs)

# Penerbit Views
class PenerbitListView(ListView):
    model = Penerbit
    template_name = 'buku/penerbit_list.html'
    context_object_name = 'penerbit_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nama_penerbit__icontains=search_query) |
                Q(kota__icontains=search_query)
            )
        return queryset

class PenerbitDetailView(DetailView):
    model = Penerbit
    template_name = 'buku/penerbit_detail.html'
    context_object_name = 'penerbit'

class PenerbitCreateView(LoginRequiredMixin, CreateView):
    model = Penerbit
    form_class = PenerbitForm
    template_name = 'buku/penerbit_form.html'
    success_url = reverse_lazy('penerbit-list')

    def form_valid(self, form):
        messages.success(self.request, 'Penerbit berhasil ditambahkan!')
        return super().form_valid(form)

class PenerbitUpdateView(LoginRequiredMixin, UpdateView):
    model = Penerbit
    form_class = PenerbitForm
    template_name = 'buku/penerbit_form.html'
    success_url = reverse_lazy('penerbit-list')

    def form_valid(self, form):
        messages.success(self.request, 'Penerbit berhasil diperbarui!')
        return super().form_valid(form)

class PenerbitDeleteView(LoginRequiredMixin, DeleteView):
    model = Penerbit
    template_name = 'buku/penerbit_confirm_delete.html'
    success_url = reverse_lazy('penerbit-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Penerbit berhasil dihapus!')
        return super().delete(request, *args, **kwargs)

# Rak Buku Views
class RakBukuListView(ListView):
    model = RakBuku
    template_name = 'buku/rak_list.html'
    context_object_name = 'rak_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nama_rak__icontains=search_query) |
                Q(lokasi_rak__icontains=search_query)
            )
        return queryset

class RakBukuDetailView(DetailView):
    model = RakBuku
    template_name = 'buku/rak_detail.html'
    context_object_name = 'rak'

class RakBukuCreateView(LoginRequiredMixin, CreateView):
    model = RakBuku
    form_class = RakBukuForm
    template_name = 'buku/rak_form.html'
    success_url = reverse_lazy('rak-list')

    def form_valid(self, form):
        messages.success(self.request, 'Rak buku berhasil ditambahkan!')
        return super().form_valid(form)

class RakBukuUpdateView(LoginRequiredMixin, UpdateView):
    model = RakBuku
    form_class = RakBukuForm
    template_name = 'buku/rak_form.html'
    success_url = reverse_lazy('rak-list')

    def form_valid(self, form):
        messages.success(self.request, 'Rak buku berhasil diperbarui!')
        return super().form_valid(form)

class RakBukuDeleteView(LoginRequiredMixin, DeleteView):
    model = RakBuku
    template_name = 'buku/rak_confirm_delete.html'
    success_url = reverse_lazy('rak-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Rak buku berhasil dihapus!')
        return super().delete(request, *args, **kwargs)

# Penempatan Buku Views
@login_required
def tambah_penempatan(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    if request.method == 'POST':
        form = PenempatanBukuForm(request.POST)
        if form.is_valid():
            penempatan = form.save(commit=False)
            penempatan.buku = buku
            penempatan.save()
            messages.success(request, 'Buku berhasil ditempatkan di rak!')
            return redirect('buku-detail', slug=buku.slug)
    else:
        form = PenempatanBukuForm()
        # Get all racks that don't have this book
        available_racks = RakBuku.objects.exclude(buku=buku)
        # Filter racks that have available capacity
        racks_with_capacity = [
            rak for rak in available_racks 
            if rak.jumlah_buku < rak.kapasitas
        ]
        form.fields['rak'].queryset = RakBuku.objects.filter(
            id__in=[rak.id for rak in racks_with_capacity]
        )
    return render(request, 'buku/penempatan_form.html', {
        'form': form, 
        'buku': buku,
        'rak': form.fields['rak'].queryset.first() if form.fields['rak'].queryset.exists() else None
    })

@login_required
def hapus_penempatan(request, penempatan_id):
    penempatan = get_object_or_404(PenempatanBuku, id=penempatan_id)
    buku = penempatan.buku
    penempatan.delete()
    messages.success(request, 'Penempatan buku berhasil dihapus!')
    return redirect('buku-detail', slug=buku.slug)

class PenempatanBukuCreateView(LoginRequiredMixin, CreateView):
    model = PenempatanBuku
    fields = ['buku']
    template_name = 'buku/penempatan_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rak_slug = self.kwargs.get('rak_slug')
        if rak_slug:
            context['rak'] = get_object_or_404(RakBuku, slug=rak_slug)
            # Filter out books that are already in this shelf
            context['form'].fields['buku'].queryset = Buku.objects.exclude(
                rak=context['rak']
            )
        return context

    def form_valid(self, form):
        rak_slug = self.kwargs.get('rak_slug')
        if rak_slug:
            form.instance.rak = get_object_or_404(RakBuku, slug=rak_slug)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('rak-detail', kwargs={'slug': self.object.rak.slug})

class PenempatanBukuDeleteView(LoginRequiredMixin, DeleteView):
    model = PenempatanBuku
    template_name = 'buku/penempatan_confirm_delete.html'

    def get_success_url(self):
        return reverse('rak-detail', kwargs={'slug': self.object.rak.slug})
