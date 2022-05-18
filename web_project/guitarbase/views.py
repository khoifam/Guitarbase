from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from .forms import *


# Create your views here.
def home(request):
    context = { 
        'artists': Artist.objects.all() , 
        'songs': Song.objects.all(),
        'verses': Verse.objects.all(),
        'choruses': Chorus.objects.all(),
        'bridge': Bridge.objects.all(),
        'artist_form' : ArtistForm(),
        'song_form' : SongForm(),
        'verse_form' : VerseForm(),
        'chorus_form' : ChorusForm(),
        'bridge_form' : BridgeForm(),
    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print('________START: AJAX FORM SAVE')
        artist_form = ArtistForm(request.POST)
        song_form = SongForm(request.POST)
        verse_form = VerseForm(request.POST)
        chorus_form = ChorusForm(request.POST)
        bridge_form = BridgeForm(request.POST)
        data = {}
        artist_form_valid = artist_form.is_valid()
        song_form_valid = song_form.is_valid()
        verse_form_valid = verse_form.is_valid()
        chorus_form_valid = chorus_form.is_valid()
        bridge_form_valid = bridge_form.is_valid()
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(str(artist_form_valid) + str(song_form_valid) + str(verse_form_valid) + str(chorus_form_valid) + str(bridge_form_valid))
        
        if artist_form_valid and song_form_valid and verse_form_valid and chorus_form_valid and bridge_form_valid:
            artist_form_pending = artist_form.save(commit=False)
            if Artist.objects.filter(artist_name=artist_form_pending.artist_name).exists():
                song_form_pending = song_form.save(commit=False)
                song_form_pending.artist = Artist.objects.get(artist_name=artist_form_pending.artist_name)
                song_form_pending.save()
                artist_preexisted = True                  
            else:
                artist_form_pending.save()

                song_form_pending = song_form.save(commit=False)
                song_form_pending.artist = artist_form_pending
                song_form_pending.save()
                artist_preexisted = False

            verse_form_pending = verse_form.save(commit=False)
            if not verse_form_pending.verse_chord_prog == '':
                verse_form_pending.song = song_form_pending
                verse_form_pending.save()
            

            chorus_form_pending = chorus_form.save(commit=False)
            if not chorus_form_pending.chorus_chord_prog == '':
                chorus_form_pending.song = song_form_pending
                chorus_form_pending.save()

            bridge_form_pending = bridge_form.save(commit=False)
            if not bridge_form_pending.bridge_chord_prog == '':
                bridge_form_pending.song = song_form_pending
                bridge_form_pending.save()

            data['artist_name'] = artist_form.cleaned_data.get('artist_name')
            data['song_name'] = song_form.cleaned_data.get('song_name')
            data['capo'] = song_form.cleaned_data.get('capo')
            data['tuning'] = song_form.cleaned_data.get('tuning')
            data['url'] = song_form.cleaned_data.get('url')
            data['verse_chord_prog'] = verse_form.cleaned_data.get('verse_chord_prog')
            data['chorus_chord_prog'] = chorus_form.cleaned_data.get('chorus_chord_prog')
            data['bridge_chord_prog'] = bridge_form.cleaned_data.get('bridge_chord_prog')
            data['artist_id'] = Artist.objects.filter(artist_name=artist_form_pending.artist_name).get().id
            data['song_id'] = Song.objects.get(song_name=song_form_pending.song_name, artist=Artist.objects.filter(artist_name=artist_form_pending.artist_name).get()).id
            data['artist_preexisted'] = artist_preexisted
            data['status'] = 'ok'
            print('________END: AJAX FORM SAVE ADDED')
            return JsonResponse(data)
            

    # if request.method == 'POST':
    #     print('________START: NON-AJAX FORM SAVE')
    #     artist_form = ArtistForm(request.POST)
    #     song_form = SongForm(request.POST)
    #     verse_form = VerseForm(request.POST)
    #     chorus_form = ChorusForm(request.POST)
    #     bridge_form = BridgeForm(request.POST)

    #     artist_form_valid = artist_form.is_valid()
    #     song_form_valid = song_form.is_valid()
    #     verse_form_valid = verse_form.is_valid()
    #     chorus_form_valid = chorus_form.is_valid()
    #     bridge_form_valid = bridge_form.is_valid()

    #     if artist_form_valid and song_form_valid and verse_form_valid and chorus_form_valid and bridge_form_valid:
    #         artist_form_pending = artist_form.save(commit=False)
    #         if Artist.objects.filter(artist_name=artist_form_pending.artist_name).exists():
    #             song_form_pending = song_form.save(commit=False)
    #             song_form_pending.artist = Artist.objects.get(artist_name=artist_form_pending.artist_name)
    #             song_form_pending.save()                  
    #         else:
    #             artist_form_pending.save()

    #             song_form_pending = song_form.save(commit=False)
    #             song_form_pending.artist = artist_form_pending
    #             song_form_pending.save()

    #         verse_form_pending = verse_form.save(commit=False)
    #         if not verse_form_pending.verse_chord_prog == '':
    #             verse_form_pending.song = song_form_pending
    #             verse_form_pending.save()
            

    #         chorus_form_pending = chorus_form.save(commit=False)
    #         if not chorus_form_pending.chorus_chord_prog == '':
    #             chorus_form_pending.song = song_form_pending
    #             chorus_form_pending.save()

    #         bridge_form_pending = bridge_form.save(commit=False)
    #         if not bridge_form_pending.bridge_chord_prog == '':
    #             bridge_form_pending.song = song_form_pending
    #             bridge_form_pending.save()
        
    #     print('________END: NON-AJAX FORM SAVE ADDED')
    #     return redirect('/guitarbase/')
        
    print('________END: FORM SAVE RENDERED')
    return render(request, 'guitarbase\home.html', context)

def delete_artist(request, pk):
    print('________START: NON-AJAX DELETE ARTIST')
    artist = Artist.objects.get(id=pk)
    
    if request.method == "POST":
        artist.delete()
        print('________END: NON-AJAX DELETE ARTIST DELETED')
        return redirect('/guitarbase/')

    context = { 'artist' : artist }
    print('________END: NON-AJAX DELETE ARTIST NOT DELETED')
    return render(request, 'guitarbase\home.html', context)

def delete_song(request, pk):
    print('________START: NON-AJAX DELETE SONG')
    song = Song.objects.get(id=pk)
    
    if request.method == "POST":
        song.delete()
        print('________END: NON-AJAX DELETE SONG DELETED')
        return redirect('/guitarbase/')

    context = { 'song' : song }
    print('________END: NON-AJAX DELETE SONG NOT DELETED')
    return render(request, 'guitarbase\home.html', context)

# edit/update songs only, artists are set in stone
# can we detect if the song name of an artist already exist, can we save the form to overwrite existing data? 
# maybe delete() and then save()
