import replicate
from PIL import Image
import os
import requests
from datetime import datetime

def text2image(text, init_img=None, show=False):

    model = replicate.models.get("cjwbw/stable-diffusion-v2")
    version = model.versions.get("e5e1fd333a08c8035974a01dd42f799f1cca4625aec374643d716d9ae40cf2e4")

    # https://replicate.com/cjwbw/stable-diffusion-v2/versions/e5e1fd333a08c8035974a01dd42f799f1cca4625aec374643d716d9ae40cf2e4#input
    inputs = {
        # Input prompt
        'prompt': text,

        # The prompt NOT to guide the image generation. Ignored when not using guidance
        # 'negative_prompt': ...,

        # Width of output image. Maximum size is 1024x768 or 768x1024 because of memory limits
        'width': 768,

        # Height of output image. Maximum size is 1024x768 or 768x1024 because of memory limits
        'height': 768,

        # Initial image to generate variations of. Will be resized to the specified width and height
        # 'init_image': open("path/to/file", "rb"),

        # Prompt strength when using init image. 1.0 corresponds to full
        # destruction of information in init image
        'prompt_strength': 0.8,

        # Number of images to output. Currenly allowing 1-3, otherwise would OOM.
        # Range: 1 to 3
        'num_outputs': 1,

        # Number of denoising steps
        # Range: 1 to 500
        'num_inference_steps': 50,

        # Scale for classifier-free guidance
        # Range: 1 to 20
        'guidance_scale': 7.5,

        # Choose a scheduler. Seems only DDIM and K_EULER and DPMSolverMultistep work for sd-v2 now.
        'scheduler': "K_EULER",

        # Random seed. Leave blank to randomize the seed
        # 'seed': ...,
    }

    if init_img:
        inputs['init_image'] = open(init_img, "rb")

    # https://replicate.com/cjwbw/stable-diffusion-v2/versions/e5e1fd333a08c8035974a01dd42f799f1cca4625aec374643d716d9ae40cf2e4#output-schema
    urls = version.predict(**inputs)
    image_data = requests.get(urls[0]).content
    image_save_folder = "./images/out"
    now = datetime.now()
    image_path = os.path.join(image_save_folder, 'sd2_' + now.strftime('%Y-%m-%d_%H-%M-%S') + '.png')
    with open(image_path, 'wb') as f:
        f.write(image_data)

    if show:
        # Load the image to a PIL Image object and display it
        image = Image.open(image_path)
        image.show()

    return image_path

if __name__ == '__main__':
    text2image("A dog eating pizza", show=True)
