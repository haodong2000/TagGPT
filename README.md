# TagGPT

TagGPT: A simple ChatGPT based multimodal dialog generation engine that can "see" and "hear"

Tag: **T**ext, **a**udio, and **g**raph

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

## Demo / usage



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
│   |   ├── 
|   |   └── 
|   └── out
│   |   ├── 
|   |   └── 
├── images
│   ├── in
│   |   ├── 
|   |   └── 
|   └── out
│   |   ├── 
|   |   └── 
└── run_gpt_3.5.py
```

## Tips

1. if you meet with `requests.exceptions.ConnectionError`, change `http` to `https` in `./AIGC/utils.py` might help :)
