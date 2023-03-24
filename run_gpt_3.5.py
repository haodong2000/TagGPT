# export OPENAI_API_KEY='sk-...'
import openai
from AIGC.clip_interrogator import image2text
from AIGC.dall_e2 import text2image as text2image_de2
from AIGC.stable_diffusion_2 import text2image as text2image_sd2
from AIGC.transcribe import audio2text
from AIGC.gtts_t2a import text2audio

def get_input(end="END"):
    input_msg = ""
    print("\nYou: ", end="")
    while True:
        current_input = input()
        input_msg += current_input + "\n"
        if current_input[-len(end):] == end:
            break
    print("-"*80)
    input_msg = input_msg[:-len(end) - 1]

    if '[[[' in input_msg:
        sub_msg = input_msg.split('[[[')
        for i in range(1, len(sub_msg)):
            image_path = sub_msg[i].split(']]]')[0]
            image_text = image2text(image_path)
            input_msg = input_msg.replace(image_path, image_text)
    if '<<<' in input_msg:
        sub_msg = input_msg.split('<<<')
        for i in range(1, len(sub_msg)):
            audio_path = sub_msg[i].split('>>>')[0]
            audio_text = audio2text(audio_path)
            input_msg = input_msg.replace(audio_path, audio_text)

    return input_msg

# I want ChatGPT to see and hear :-)
messages = [
    {"role": "system", "content": "You can see images through the description, and you can draw images by describing them in '[[[' and ']]]'. For example, '[[[a cat]]]' will draw a cat. You can also draw multiple images, like `[[[a beautiful flower]]], [[[a big shark]]]`. Remember, any text between '[[[' and ']]]' is the description of a picture."},
    {"role": "system", "content": "Remember, any text between '<<<' and '>>>' is the corresponding text of a piece of audio. You can pretend to hear any audio through its corresponding text, and you can speak by putting the corresponding text in '<<<' and '>>>', for example, '<<<wow, you are beautiful!>>>' will speak: \"wow, you are beautiful!\". You can also speak multiple audios, like `<<<hello, how are you?>>> <<<I'm fine, thank you.>>>`. Remember, once the user speaks to you, you should speak back."}]

user_text = get_input()

def no_br_in_begin(reply):
    for i in range(len(reply)):
        if reply[i] != '\n':
            return reply[i:]
    raise KeyboardInterrupt

def interact_with_ChatGPT():
    global messages, user_text

    # I want this code to run indefinitely, until any of the parties say Thank You
    while user_text not in ["", "q", "Q", "\n", "q\n", "Q\n"]:
        messages.append({"role": "user", "content": user_text})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = response.choices[0].message.content

        if '[[[' in reply:
            sub_msg = reply.split('[[[')
            for i in range(1, len(sub_msg)):
                image_desc = sub_msg[i].split(']]]')[0]
                image_path = text2image_sd2(image_desc)
                reply = reply.replace(image_desc, image_path)
        if '<<<' in reply:
            sub_msg = reply.split('<<<')
            for i in range(1, len(sub_msg)):
                audio_desc = sub_msg[i].split('>>>')[0]
                audio_path = text2audio(audio_desc)
                reply = reply.replace(audio_desc, audio_path)

        print("\nChatGPT:", no_br_in_begin(reply), end="\n"+"-"*80+"\n")
        messages.append({"role": "assistant", "content": reply})
        user_text = get_input()

interact_with_ChatGPT()

"""
1

Here is a picture [[[./images/in/dogpizza.jpg]]], replace the dogs with white cute cats.END

Give me one similar image, thanksEND

Give me 3 images about wild animals in deep oceanEND

Please discribe the first one and speak to meEND

Here is another picture [[[./images/in/elon.png]]], tell me how many peoples are there?END

END
"""

"""
2

<<<./audios/in/haodong.mp3>>>END

here is a piece of audio, <<<./audios/in/assemblyai.mp3>>>.
please writa a short report about AssemblyAIEND

What could we do using assemblyai api? give me a list, and speak it to me.
END

design a logo for assemblyai, and draw it based on your description

END
"""
