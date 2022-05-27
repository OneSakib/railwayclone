from django.urls import path
from . import views

app_name = 'IR'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('pnrenquiry/', views.PNREnquiry.as_view(), name='pnrenquiry'),
    path('pnrenqresult/', views.PNREnqResult.as_view(), name='pnrenqresult'),
    path('reservedtbs/', views.ReservedTBS.as_view(), name='reservedtbs'),
    path('seata/', views.SeatA.as_view(), name='seata'),
    path('fareenq/', views.FareEnq.as_view(), name='fareenq'),
    path('reservedtrainschedule/', views.ReservedTrainSchedule.as_view(), name='reservedtrainschedule'),
    path('reservedtrain/', views.Reservation.as_view(), name='reservedtrain'),
    path('mobiletrack/', views.MobileTrack.as_view(), name='mobiletrack'),
    path('ftr/', views.FTR.as_view(), name='ftr'),
    path('sms/', views.SMS.as_view(), name='sms'),
    path('luxerytrain/', views.LuxuryTrain.as_view(), name='luxerytrain'),
    path('specialhill/', views.SpecialHill.as_view(), name='specialhill'),
    path('cateringcharg/', views.CateringCharges.as_view(), name='cateringcharg'),
    path('quotacode/', views.QuotaCodes.as_view(), name='quotacode'),
    path('tatkal/', views.TatkalScheme.as_view(), name='tatkal'),
    path('reservation/', views.Reservation.as_view(), name='reservation'),
    path('refund/', views.Refund.as_view(), name='refund'),
    path('other/', views.OtherRules.as_view(), name='other'),
    path('luggage/', views.Luggage.as_view(), name='luggage'),
    path('internationaltourist/', views.InternationalTourists.as_view(), name='internationaltourist'),
    path('otherrailwaywebsite/', views.OtherRailwaywebsite.as_view(), name='otherrailwaywebsite'),
    path('gettrainresult/', views.GetTrainResult.as_view(), name='gettrainresult')
]
