from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404

from vaccine.models import Vaccine
from vaccine.forms import VaccineForm


class VaccineList(View):
    def get(self, request):
        vaccine_list = Vaccine.objects.all()
        context = {
            "objects_list": vaccine_list
        }
        return render(request, "vaccine/vaccine-list.html", context)


class VaccineDetail(View):
    def get(self, request, id):
        try:
            vaccine = Vaccine.objects.get(id=id)
        except Vaccine.DoesNotExist:
            raise Http404("Vaccine instance not found.")
        context = {
            'object': vaccine
        }
        return render(request, "vaccine/vaccine-detail.html", context)


class VaccineCreate(View):
    form_class = VaccineForm
    template_name = "vaccine/vaccine-create.html"

    def get(self, request):
        context = {
            "form": self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("vaccine:list"))
        return render(request, self.template_name, {"form": form})


class VaccineUpdate(View):
    form_class = VaccineForm
    template_name = 'vaccine/vaccine-update.html'

    def get(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        context = {
            "form": self.form_class(instance=vaccine)
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        form = self.form_class(request.POST, instance=vaccine)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("vaccine:detail", kwargs={"id": vaccine.id}))
        return render(request, self.template_name, {"form": form})


class VaccineDelete(View):
    template_name = "vaccine/vaccine-delete.html"

    def get(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        context = {
            "object": vaccine
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        Vaccine.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse("vaccine:list"))


