from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        summary = summarize_text(text)
    return render_template('index.html', summary=summary)

def summarize_text(text):
    # Generate a summary of the text
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == '__main__':
    app.run(debug=True)
