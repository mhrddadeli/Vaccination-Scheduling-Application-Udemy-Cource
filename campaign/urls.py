from django.urls import path

from campaign.views import CampaignListView, CampaignDetailView, CampaignCreateView, CampaignUpdateView, \
    CampaignDeleteView, SlotListView, SlotDetailView, SlotCreateView, SlotUpdateView, SlotDeleteView

app_name = 'campaign'

urlpatterns = [
    path('', CampaignListView.as_view(), name='campaign-list'),
    path('<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    path('create/', CampaignCreateView.as_view(), name='campaign-create'),
    path('update/<int:pk>/', CampaignUpdateView.as_view(), name='campaign-update'),
    path('delete/<int:pk>/', CampaignDeleteView.as_view(), name='campaign-delete'),
    path('<int:campaign_id>/slot/', SlotListView.as_view(), name='slot-list'),
    path('slot/<int:pk>/', SlotDetailView.as_view(), name='slot-detail'),
    path('<int:campaign_id>/slot/create/', SlotCreateView.as_view(), name='slot-create'),
    path('<int:campaign_id>/slot/update/<int:pk>/', SlotUpdateView.as_view(), name='slot-update'),
    path('<int:campaign_id>/slot/delete/<int:pk>/', SlotDeleteView.as_view(), name='slot-delete'),
]