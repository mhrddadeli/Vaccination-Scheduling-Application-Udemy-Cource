from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, Http404
from django.views import generic
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from center.models import Center, Storage
from center.forms import CenterForm, StorageForm


def center_list(request):
    objects = Center.objects.all().order_by("name")
    paginator = Paginator(objects, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
    }
    return render(request, "center/center-list.html", context)


def center_detail(request, id):
    object = Center.objects.get(id=id)
    context = {
        "center": object
    }
    return render(request, "center/center-detail.html", context)


def center_create(request):
    if request.method == "POST":
        form = CenterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Center Created Successfully.")
            return HttpResponseRedirect(reverse("center:list"))
        messages.error(request, "Please Enter Valid Data.")
        return render(request, "center/center-create.html", {"form": form})

    # GET
    context = {
        "form": CenterForm()
    }
    return render(request, "center/center-create.html", context)


def center_update(request, id):
    try:
        center = Center.objects.get(id=id)
    except Center.DoesNotExist:
        raise Http404("Center instance is not found.")

    if request.method == "POST":
        form = CenterForm(request.POST, instance=center)
        if form.is_valid():
            form.save()
            messages.success(request, "Center Updated Successfully.")
            return HttpResponseRedirect(reverse("center:detail", kwargs={"id": center.id}))
        messages.error(request, "Please Enter Valid Data.")
        return render(request, "center/center-update.html", {"form": form})
    # get
    context = {
        "form": CenterForm(instance=center)
    }
    return render(request, "center/center-update.html", context)


def center_delete(request, id):
    try:
        center = Center.objects.get(id=id)
    except Center.DoesNotExist:
        raise Http404("Center instance is not found.")

    if request.method == "POST":
        center.delete()
        messages.success(request, "Center Deleted Successfully.")
        return HttpResponseRedirect(reverse("center:list"))

    # get
    context = {
        "center": center
    }
    return render(request, "center/center-delete.html", context)


# storage generic class base views


class StorageList(generic.ListView):
    queryset = Storage.objects.all()
    template_name = "storage/storage-list.html"
    ordering = ["id"]
    paginate_by = 3

    def get_queryset(self):
        center_id = self.kwargs["center_id"]
        return super().get_queryset().filter(center_id=center_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["center_id"] = self.kwargs["center_id"]
        return context


class StorageDetail(generic.DetailView):
    model = Storage
    template_name = "storage/storage-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        available_quantity = self.object.total_quantity - self.object.booked_quantity
        context["available_quantity"] = available_quantity
        return context


class StorageCreate(SuccessMessageMixin, generic.CreateView):
    model = Storage
    form_class = StorageForm
    template_name = "storage/storage-create.html"
    success_message = "Storage Created Successfully"

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["center_id"] = self.kwargs["center_id"]
    #     return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial["center"] = Center.objects.get(id=self.kwargs["center_id"])
        return initial

    def get_success_url(self):
        return reverse("center:storage-list", kwargs={'center_id': self.kwargs["center_id"]})


class StorageUpdate(SuccessMessageMixin, generic.UpdateView):
    model = Storage
    form_class = StorageForm
    template_name = "storage/storage-update.html"
    success_message = "Storage Updated Successfully"

    def get_success_url(self):
        return reverse("center:storage-list", kwargs={'center_id': self.get_object().center.id})


class StorageDelete(SuccessMessageMixin, generic.DeleteView):
    model = Storage
    template_name = "storage/storage-delete.html"
    success_message = "Storage Deleted Successfully"

    def get_success_url(self):
        return reverse("center:storage-list", kwargs={'center_id': self.get_object().center.id})