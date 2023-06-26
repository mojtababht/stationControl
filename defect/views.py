from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from django.urls import reverse_lazy


class Stations(ListView):
    model=Station
    template_name= "station.html"


class Faults(ListView):
    model=Fault
    template_name="faults.html"


class StationDetail(DetailView):
    model=Station
    template_name='stationdetail.html'





class FaultDetail(DetailView):
    model=Fault
    template_name="faultdetail.html"

class StationCreate(CreateView):
    model = Station
    template_name = "stationcreate.html"
    fields= '__all__'
    
class ReportCreate(CreateView):
    model=Report
    fields="__all__"
    template_name='reportcreate.html' 
    # success_url='/'     
    def get_success_url(self):
        return reverse_lazy('stationdetail',args=(int(self.request.POST.get('station')),))   

class FaultCreate(CreateView):
    model = Fault
    template_name = "faultcreate.html"
    fields= '__all__'
    

class StationUpdate(UpdateView):
    model = Station
    template_name = "stationupdate.html"
    fields='__all__'


class FaultUpdate(UpdateView):
    model = Fault
    template_name = "faultupdate.html"
    fields='__all__'


class ReportUpdate(UpdateView):
    model=Report
    template_name='reportupdate.html'
    fields='__all__'
    def get_success_url(self):
        return reverse_lazy('stationdetail',args=(self.object.station.id,))


class StationDelete(DeleteView):
    model = Station
    template_name = "stationdelete.html"
    success_url=reverse_lazy('stations')

class FaultDelete(DeleteView):
    model = Fault
    template_name = "faultdelete.html"
    success_url=reverse_lazy('faults')


class ReportDelete(DeleteView):
    model=Report
    template_name='reportdelete.html'
    def get_success_url(self) :
        return reverse_lazy('stationdetail',args=(self.object.station.id,))






class Pieces(ListView):
    model=Piece
    template_name='pieces.html'



class PieceCreate(CreateView):
    model=Piece
    template_name='piececreate.html'
    fields='__all__'
    success_url=reverse_lazy('pieces')


class PieceUpdate(UpdateView):
    model=Piece
    template_name='pieceupdate.html'
    fields='__all__'
    success_url=reverse_lazy('pieces')



class PieceDelete(DeleteView):
    model=Piece
    template_name='piecedelete.html'
    success_url=reverse_lazy('pieces')