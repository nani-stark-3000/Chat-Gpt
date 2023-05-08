from flask import Flask, render_template, request
import requests
import openai

openai.api_key = "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"

def Generate(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("Error:", e)
        return "Sorry, I could not generate a response."


app = Flask(__name__,template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['prompt']
        answer = Generate(f"User: {input_text}\nChatGPT:")
        return render_template('index.html', answer=answer)
    else:
        return render_template('index.html')
    
if '__main__'==__name__:
    app.run(port=34,debug=True)
