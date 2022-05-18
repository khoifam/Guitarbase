console.log('START OF MAIN.JS');
const form = document.getElementById('form');

const artistName = document.getElementById('id_artist_name');
const songName = document.getElementById('id_song_name');
const capo = document.getElementById('id_capo');
const tuning = document.getElementById('id_tuning');
const songUrl = document.getElementById('id_url');
const verseChord = document.getElementById('id_verse_chord_prog');
const chorusChord = document.getElementById('id_chorus_chord_prog');
const bridgeChord = document.getElementById('id_bridge_chord_prog');

const url = "";

const csrf = document.getElementsByName('csrfmiddlewaretoken');
console.log(csrf);

form.addEventListener('submit', e=>{
    console.log('EVENT LISTENER FUNCTION BEGINS')
    e.preventDefault();

    const myFormData = new FormData();
    myFormData.append('csrfmiddlewaretoken', csrf[0].value);
    myFormData.append('artist_name', artistName.value)
    myFormData.append('song_name', songName.value)
    myFormData.append('capo', capo.value)
    myFormData.append('tuning', tuning.value)
    myFormData.append('url', songUrl.value)
    myFormData.append('verse_chord_prog', verseChord.value)
    myFormData.append('chorus_chord_prog', chorusChord.value)
    myFormData.append('bridge_chord_prog', bridgeChord.value)

    console.log('FORM DATA APPENDED');

    console.log('AJAX FUNCTION BEGINS')

    $.ajax({
        method: 'POST',
        type: 'POST',
        headers: {"X-Requested-With": "XMLHttpRequest", "X-CSRFToken": getCookie(csrf)},
        url: url,
        enctype: 'multipart/form-data',
        data: myFormData,
        success: function(data) {
            console.log(data);
            $('#container').append(
                "<article class = content-artist><h2>" + data.artist_name + "</h2><form class='button' method='POST' action=''><input type='hidden' name='csrfmiddlewaretoken' value='" + getCookie("csrftoken") + "'><input type='submit' value='Delete'></form><form class='button'><input type='submit' value='Edit'></form></article>",
                "<div class = div-contain><section class = content-song><h3>" + data.song_name + "</h3><form class='button' method='POST' action='{% url 'guitarbase-delete-song' song.id %}'><input type='submit' value='Delete'></form><form class='button'><input type='submit' value='Edit'></form></section><div class = div-contain><section class = content-info><p>Capo: " + data.capo + ", Tuning: " + data.tuning + "</p></section></div></div>"
            )
            addEventsToAccordion();
        },
        error: function(error) {
            console.log(error);
        },
        cache: false,
        contentType: false,
        processData: false,
    });

    console.log('AJAX FUNCTION CALLED')
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');