# TagGPT

**[Demos](https://lebronlihd.github.io/blog/2023/demos-of-taggpt/) | [Prompt](https://lebronlihd.github.io/projects/taggpt/)**

<img src="https://user-images.githubusercontent.com/67775090/227708815-8c4baf62-73de-4b03-8e3c-3b16980aa0d5.jpeg" width="400">

- **T**ext-**a**udio-**g**raph GPT: A simple ChatGPT based multimodal dialog generation engine that can
  - "see" through [clip-interrogator](https://replicate.com/pharmapsychotic/clip-interrogator),
  - "draw" through [stable-diffusion-v2](https://replicate.com/cjwbw/stable-diffusion-v2),
  - "hear" through [assemblyai-transcript](https://www.assemblyai.com/),
  - and "speak" through [gTTS](https://github.com/pndurette/gTTS)

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

## Demos

- **[Please see full demos here](https://lebronlihd.github.io/blog/2023/demos-of-taggpt/)**

## Usage

- Images are expressed as `[[[./path/to/image]]]`
- Audios are expressed as `<<<./path/to/audio>>>`
- `END` is the end-of-input marker
- Examples:

```
You: Here is a picture [[[./images/in/dogpizza.jpg]]], replace the dogs with white cute cats.
END

ChatGPT: Here is your updated picture: [[[./images/out/sd2_2023-03-25_12-49-24.png]]]. Enjoy!
```

```
You: <<<./audios/in/assemblyai.mp3>>>
please help me writa a short introduction about AssemblyAI END

ChatGPT: AssemblyAI is a deep learning company that ...
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

## To-do

- Build a UI (maybe)

## Tips

1. if you meet with `requests.exceptions.ConnectionError`, change `http` to `https` in `./AIGC/utils.py` might help :)
