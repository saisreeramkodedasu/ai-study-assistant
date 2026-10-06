import tempfile
from gtts import gTTS


def text_to_speech(text):

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    temp_file.close()

    tts = gTTS(
        text=text,
        lang="en"
    )

    tts.save(temp_file.name)

    return temp_file.name