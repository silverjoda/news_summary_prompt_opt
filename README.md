# Project Setup Instructions

Follow these steps to set up the project environment and install the necessary dependencies.

## Create a Python Virtual Environment

1. Create a new Python virtual environment:
    ```sh
    python -m venv .venvinitial_system_promptu
    ```

2. Activate the virtual environment:
    ```sh
    source .venv/bin/activate
    ```

## Install the Project

1. Install the project in editable mode:
    ```sh
    pip install -e .
    ```

2. Install additional dependencies from `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

## API Keys

1. Create a `.env` file in the project root directory.
2. Add your OpenAI API key to the `.env` file:
    ```sh
    OPENAI_API_KEY="your_openai_api_key_here"
    ```

## Configuration

- Use the `config.json` file to configure training parameters and prompts


## Guidelines

- For decent result I think that we need at least 20-30 quality examples
- The data provided has some issues, such as the summary containing information about events and names that are not even in the news
- Try 1-3 epochs.