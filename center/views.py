from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, Http404

from center.models import Center
from center.forms import CenterForm


def center_list(request):
    objects = Center.objects.all()
    context = {
        "center": objects
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
            return HttpResponseRedirect(reverse("center:list"))
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
        form = CenterForm(instance=center)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("center:detail", kwargs={"id": center.id}))
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
        return HttpResponseRedirect(reverse("center:list"))
    # get
    context = {
        "center": center
    }
    return render(request, "center/center-delete.html", context)
