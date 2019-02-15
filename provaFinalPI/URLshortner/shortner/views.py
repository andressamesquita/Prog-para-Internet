from django.shortcuts import render, redirect
from django.views.generic.base import View
from shortner.forms import UrlForm
from shortner.models import Url 
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from shortner.serializers import UrlSerializer


def index(request):

    form = UrlForm()
    return render(request, "index.html", {'form': form})


class UrlView(View):

    def post(self, request):

        form = UrlForm(request.POST)
        
        if form.is_valid():
           
            dados_form = form.cleaned_data
            url = Url()
            url.texto_url = dados_form['texto_url']
            url.url_encurtada = url.encurta_url()
            url.save()
            return render(request, 'index.html', {'form':form, 'url':url} )
            

        return redirect('index')

def desencurtar(request, encurtada):

    enc = 'http://localhost:8000/'+ encurtada
    url = Url.objects.get(url_encurtada = enc)
    return redirect(url.texto_url)


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def create(self, request, pk=None):
        serialized_data = UrlSerializer(data=request.data)

        if serialized_data.is_valid():
            try:
                url = Url()
                url.texto_url = serialized_data.data['texto_url']
                url.url_encurtada = url.encurta_url()
                
                if(len(url.texto_url) < (len(url.url_encurtada))):
                    return Response({'error': 'Impossível encurtar url'}, status=status.HTTP_400_BAD_REQUEST)
                url.save()

                return Response({'url_encurtada': url.url_encurtada})
            
            except:
                return Response({'error': 'Impossível encurtar url'}, status=status.HTTP_400_BAD_REQUEST)
            

    
