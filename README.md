# TagGPT

- TagGPT: A simple ChatGPT based multimodal dialog generation engine that can
  - "see" through [clip-interrogator](https://replicate.com/pharmapsychotic/clip-interrogator),
  - "draw" through [stable-diffusion-v2](https://replicate.com/cjwbw/stable-diffusion-v2),
  - "hear" through [assemblyai-transcript](https://www.assemblyai.com/),
  - and "speak" through [gTTS](https://github.com/pndurette/gTTS)
- Tag: **T**ext, **a**udio, and **g**raph

## Configuration

1. Add your `API_KEY` for `OPENAI`, `REPLICATE`, and `AAI` into the environment variables

```
export OPENAI_API_KEY='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'
export REPLICATE_API_TOKEN='1bfc2afabff6319bb16a80cff8ca2b693c06d383'
export AAI_API_KEY='14aa7acd8e694265b4e51a65247f9a19'
```

2. Install required packages

```
openai
replicate
gtts
requests
datetime
pillow
time
```

## Demos & usage

- Images are expressed as `[[[./path/to/image]]]`
- Audios are expressed as `<<<./path/to/audio>>>`
- `END` is the end-of-input marker

```
You: Here is a picture [[[./images/in/dogpizza.jpg]]], replace the dogs with white cute cats.
END

ChatGPT: Here is your updated picture: [[[./images/out/sd2_2023-03-25_12-49-24.png]]]. Enjoy!
```

```
You: give me three images about city scenariosEND

ChatGPT: Sure! Here are three images about city scenarios:
[[[./images/out/sd2_2023-03-25_12-50-36.png]]], [[[./images/out/sd2_2023-03-25_12-50-46.png]]], [[[./images/out/sd2_2023-03-25_12-50-56.png]]].

You: discribe the last one and speak your answerEND

ChatGPT: The last image shows a busy city street filled with cars, buses, and people walking on the sidewalks. The tall buildings on either side of the street create a canyon-like effect, and the sun casts long shadows across the scene. There are streetlights and traffic signals visible, indicating that this is a heavily trafficked area. Overall, it's a bustling and vibrant city scene.

As for my answer, here it is: <<<./audios/out/2023-03-25_12-51-11.mp3>>>.
```

```
You: <<<./audios/in/assemblyai.mp3>>>
please help me writa a short introduction about AssemblyAI END

ChatGPT: AssemblyAI is a deep learning company that provides powerful APIs for audio transcription and understanding. Their APIs convert audio and video into text using advanced deep learning models, allowing for automatic transcription of millions of podcasts, zoom recordings, phone calls or video files daily. AssemblyAI is particularly good at helping users understand their data, with features such as auto chapters, sentiment analysis, content safety detection, auto highlights, and entity detection. Their API is used by developers to build a wide variety of applications, such as meeting summarizers, brand safety tools, and conversational intelligence platforms.
```

## Project Structure

```
TagGPT
├── AIGC
│   ├── clip_interrogator.py
│   ├── dall_e2.py
│   ├── gtts_t2a.py
│   ├── stable_diffusion_2.py
│   └── transcribe.py
├── audios
│   ├── in
|   └── out
├── images
│   ├── in
|   └── out
└── run_gpt_3.5.py
```

## Tips

1. if you meet with `requests.exceptions.ConnectionError`, change `http` to `https` in `./AIGC/utils.py` might help :)
