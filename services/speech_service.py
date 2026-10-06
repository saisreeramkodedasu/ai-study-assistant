import tempfile
import whisper


_model = None


def load_whisper_model():

    global _model

    if _model is None:
        _model = whisper.load_model("base")

    return _model


def transcribe_audio(audio_file):

    audio_bytes = audio_file.getvalue()

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    temp_file.write(audio_bytes)
    temp_file.close()

    model = load_whisper_model()

    result = model.transcribe(temp_file.name)

    return result["text"].strip()