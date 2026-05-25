from django.urls import path

from campaign.views import CampaignListView, CampaignDetailView, CampaignCreateView, CampaignUpdateView, CampaignDeleteView

app_name = 'campaign'

urlpatterns = [
    path('', CampaignListView.as_view(), name='campaign-list'),
    path('<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    path('create/', CampaignCreateView.as_view(), name='campaign-create'),
    path('update/<int:pk>/', CampaignUpdateView.as_view(), name='campaign-update'),
    path('delete/<int:pk>/', CampaignDeleteView.as_view(), name='campaign-delete'),
]