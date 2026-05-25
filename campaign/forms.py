from django.forms import ModelForm
from campaign.models import Campaign

class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = "__all__"

    def __int__(self, *args, **kwargs):
        super(CampaignCreateForm, self).__int__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"