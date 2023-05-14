import os 
os.system("pip install tensorflow")
os.system("pip install torch")
os.system("pip install git+https://github.com/openai/whisper.git")
os.system("pip install transformers")
os.system("pip install openai")
import tensorflow
import transformers
import gradio as gr
import gradio as gr
import whisper
import openai
from share_btn import community_icon_html, loading_icon_html, share_js
from transformers import pipeline
from transformers import GPT2LMHeadModel, GPT2Tokenizer


model = whisper.load_model("small")

def fun(question):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')
    model = GPT2LMHeadModel.from_pretrained("gpt2-large",pad_token_id=tokenizer.eos_token_id)
    tokenizer.decode(tokenizer.eos_token_id)
    sentence = question
    input_ids = tokenizer.encode(sentence,return_tensors='pt')
    output = model.generate(input_ids,max_length= 100,num_beams=5,no_repeat_ngram_size=2,early_stopping=True)
    return tokenizer.decode(output[0],skip_special_tokens=True)

    
def inference(audio):
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)
    print(result.text)
    test = result.text
    answer = fun(test)
    return answer, gr.update(visible=True), gr.update(visible=True), gr.update(visible=True)



block = gr.Blocks(title='Talk to chatGPT')

with block:
    with gr.Group():
        with gr.Box():
            with gr.Row().style(mobile_collapse=False, equal_height=True):
                audio = gr.Audio(
                    label="Input Audio",
                    show_label=False,
                    source="microphone",
                    type="filepath"
                )

                btn = gr.Button("Transcribe")
        one = gr.Textbox(show_label = False,elem_id="one")
        text = gr.Textbox(show_label=True, elem_id="result-textarea")
        with gr.Group(elem_id="share-btn-container"):
            community_icon = gr.HTML(community_icon_html, visible=False)
            loading_icon = gr.HTML(loading_icon_html, visible=False)
            share_button = gr.Button("Share to community", elem_id="share-btn", visible=False)
        btn.click(inference, inputs=[audio], outputs=[text, community_icon, loading_icon, share_button])
        share_button.click(None, [], [], _js=share_js)
block.launch()
