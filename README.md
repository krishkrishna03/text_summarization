# Text Summarization Flask App

This is a simple Flask application that uses Hugging Face's Transformers library to summarize text. The application allows users to input text and receive a summarized version of the text.

## Features

- **Text Summarization**: Uses the Transformers library's summarization pipeline to generate summaries of input text.
- **Web Interface**: Simple web interface built with Flask and HTML to interact with the summarization model.

## Prerequisites

- Python 3.6 or later
- Flask
- Transformers library by Hugging Face

## Installation

1. **Clone the repository**:

    ```bash
    https://github.com/krishkrishna03/text_summarization.git
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `requirements.txt` file** with the following content:

    ```txt
    Flask
    transformers
    ```

## Running the Application

1. **Start the Flask application**:

    ```bash
    python app.py
    ```

2. **Open a web browser** and navigate to `http://127.0.0.1:5000/`.

3. **Use the web interface** to input text and get a summary.

## Code Explanation

- `app.py`: The main Flask application file that sets up the web server and handles text summarization.
- `index.html`: The HTML template used to render the input form and display the summary.

## Example Usage

1. Open the application in a web browser.
2. Enter the text you want to summarize in the input field.
3. Click the submit button to see the summarized text.

## Troubleshooting

- Ensure that all dependencies are installed correctly.
- If you encounter any issues, make sure your environment has internet access to download the model from Hugging Face.

## Contributing

Feel free to open issues or submit pull requests to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

