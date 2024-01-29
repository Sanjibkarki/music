from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404
from django.views import View
from .models import Music
from .serializers import Myserializer
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import generics
from .models import Album
from django.core.files.uploadedfile import InMemoryUploadedFile
from pydub import AudioSegment
from io import BytesIO
from rest_framework import generics,permissions,authentication
from .models import Music
from rest_framework.decorators import APIView
from .serializers import Myserializer

class Index(ListView):
    model = Music
    template_name = 'index.html'
    
class Upload(View):
    def get(self,request):
        return render(request,'post.html')

    def post(self,request):
        singer_name = request.POST['name']
        singer_image = request.FILES['image']
        data = Music(singer_name=singer_name, singer_image=singer_image)
        data.save()
        return HttpResponseRedirect(reverse('home'))

class UploadAlbums(View):
    def get(self,request,slug):
        music_instance = Music.objects.get(singer_name=slug)
        request.session['pk'] = music_instance.singer_name
        album = Album.objects.filter(singer=music_instance)
        song = None
        if album is None:
            album = Album.objects.none()
        return render(request,'albums.html',{'Album':album,'name':music_instance.singer_name,'song':song})
    

        
def lay(request,pk):
    song = Album.objects.get(id = pk)
    album = Album.objects.filter(singer=song.singer)
    return render(request,'albums.html',{'song':song,'Album':album})
    
def Add(request):
    f = request.session.get('pk')
    if request.method == 'POST':
        songname = request.POST['songname']
        song = request.FILES['song']
        songi = Music.objects.get(singer_name = f)
        a = Album(singer = songi,song_name = songname,songs= song)
        a.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request,'add.html')


def download_file(request, pk):
    file_instance = get_object_or_404(Music, id=pk)
    file_path = file_instance.music_file.path

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='audio/wav')

    response['Content-Disposition'] = f'attachment; filename="{file_instance.music_name}"'
    return response

class Api(APIView):
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request):
        users = Album.objects.all()
        serializer = Myserializer(users, many=True)
        return Response(serializer.data)

class Update(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = Myserializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser]
                
    def perform_update(self,serializer):
        instance = serializer.save()
        
def delete(request, pk):
    data = Music.objects.get(id = pk)
    data.delete()
    return HttpResponseRedirect(reverse('home'))
        
        # # Check if the file size exceeds 3MB
        # max_size = 3 * 1024 * 1024  # 3MB in bytes
        # if file.size > max_size:
        #     # Load the audio file
        #     audio = AudioSegment.from_file(file, format=file.name.split('.')[-1])

        #     # Compress the audio to reduce its size
        #     compressed_audio = audio.set_frame_rate(22050)  # Adjust the frame rate as needed

        #     # Export the compressed audio to a BytesIO buffer
        #     buffer = BytesIO()
        #     compressed_audio.export(buffer, format='wav')  # Adjust the format based on your needs
        #     buffer.seek(0)

        #     # Replace the original file with the compressed one
        #     file = InMemoryUploadedFile(buffer, None, f'{file.name}_compressed.mp3', 'audio/mp3', buffer.getbuffer().nbytes, None)
