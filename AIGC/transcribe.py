import os
import AIGC.utils as utils


def audio2text(audio_file, is_local=True, show=False):
    # Create header with authorization along with content-type
    header = {
        'authorization': os.getenv("AAI_API_KEY"),
        'content-type': 'application/json'
    }

    if is_local:
        # Upload the audio file to AssemblyAI
        upload_url = utils.upload_file(audio_file, header)
    else:
        upload_url = {'upload_url': audio_file}

    # Request a transcription
    transcript_response = utils.request_transcript(upload_url, header)

    # Create a polling endpoint that will let us check when the transcription is complete
    polling_endpoint = utils.make_polling_endpoint(transcript_response)

    # Wait until the transcription is complete
    utils.wait_for_completion(polling_endpoint, header)

    # Request the paragraphs of the transcript
    paragraphs = utils.get_paragraphs(polling_endpoint, header)

    # Save and print transcript
    transcript = ""
    for para in paragraphs:
        transcript += (para['text'] + '\n\n')
    
    if show:
        print(transcript)

    return transcript


if __name__ == '__main__':
    audio2text('https://github.com/AssemblyAI-Examples/assemblyai-and-python-in-5-minutes/raw/main/audio.mp3', 
               is_local=False)
