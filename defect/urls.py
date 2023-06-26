from django.urls import path
from .views import *

urlpatterns = [
    path('',Stations.as_view(),name='stations'),
    path('station/<int:pk>/',StationDetail.as_view(),name="stationdetail"),
    path('faults/',Faults.as_view(),name='faults'),
    path('faults/<int:pk>/',FaultDetail.as_view(),name='faultdetail'),
    path('newstation/',StationCreate.as_view(),name='stationcreate'),
    path('newfault/',FaultCreate.as_view(),name='faultcreate'),
    path('newreport/',ReportCreate.as_view(),name='reportcreate'),
    path('editstation/<int:pk>/',StationUpdate.as_view(),name='stationupdate'),
    path('editfault/<int:pk>/',FaultUpdate.as_view(),name='faultupdate'),
    path('deletestation/<int:pk>/',StationDelete.as_view(),name='stationdelete'),
    path('deleteFault/<int:pk>/',FaultDelete.as_view(),name='faultdelete'),
    path('editreport/<int:pk>/',ReportUpdate.as_view(),name='reportupdate'),
    path('deletreport/<int:pk>/',ReportDelete.as_view(),name='reportdelete'),
    path('pieces/',Pieces.as_view(),name='pieces'),
    path('newpiece/',PieceCreate.as_view(),name='piececreate'),
    path('editpiece/<int:pk>/',PieceUpdate.as_view(),name='pieceupdate'),
    path('deletepiece/<int:pk>/',PieceDelete.as_view(),name='piecedelete'),


    
] 
