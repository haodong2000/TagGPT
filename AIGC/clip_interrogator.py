import replicate

def image2text(img_path):

    model = replicate.models.get("pharmapsychotic/clip-interrogator")
    version = model.versions.get("a4a8bafd6089e1716b06057c42b19378250d008b80fe87caa5cd36d40c1eda90")

    # https://replicate.com/pharmapsychotic/clip-interrogator/versions/a4a8bafd6089e1716b06057c42b19378250d008b80fe87caa5cd36d40c1eda90#input
    inputs = {
        # Input image
        'image': open(img_path, "rb"),

        # Choose ViT-L for Stable Diffusion 1, and ViT-H for Stable Diffusion 2
        'clip_model_name': "ViT-H-14/laion2b_s32b_b79k",

        # Prompt mode (best takes 10-20 seconds, fast takes 1-2 seconds).
        'mode': "fast",
    }

    # https://replicate.com/pharmapsychotic/clip-interrogator/versions/a4a8bafd6089e1716b06057c42b19378250d008b80fe87caa5cd36d40c1eda90#output-schema
    output = version.predict(**inputs)
    return output

if __name__ == '__main__':
    image2text("./images/in/" + "Two_dogs_eating_pizza,_in_realistic_style" + ".png")
