import whisper

def transcribe(transcribing,transcribed):
    #KAMUS LOKAL:
    #model = whisper (string, boolean)
    #result = array of string
    #f = TextIOWrapper

    #Kasih 'import whisper' diatas function nya
    #Jangan lupa 'pip install whisper' dan 'pip install openai-whisper'

    model = whisper.load_model('base')
    result=model.transcribe(transcribing) #masukkin PATH file mp3/mp4 nya

    with open (transcribed,'w') as f: #Ganti 'transcribed' jadi file .txt yang lain, nanti ke overwrite
        f.write(result['text'])
    return()
