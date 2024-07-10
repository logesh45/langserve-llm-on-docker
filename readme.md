# Serve LLM using LangServe on a docker container

This project sets up a language model server using FastAPI, Docker, and Langserve. The server uses the Llama model for natural language processing tasks.


## Getting Started

### Prerequisites

- Docker
- Python 3.8 or later
- Llama model (download and add to the project folder)

### main.py

The main script that sets up and runs the FastAPI server. Replace `"your model name"` with the path to your Llama model:

```python
# Define the Llama model
llm = LlamaCpp(
    model_path="your model name",  # Specify your model path here
    temperature=0.75,
    max_tokens=2000,
    top_p=1
)
```

Optional: You can also add the model name in `local_inference.py` and `simple-flask.py` to test it without using the Docker container.


### Building and Running the Docker Container

1. **Build the Docker image**:
    ```sh
    docker build -t llama-server .
    ```

2. **Run the Docker container**:
    ```sh
    docker run -p 3000:3000 llama-server
    ```

The FastAPI server will be accessible at `http://localhost:3000`.

## Usage

### Accessing the Llama Model Endpoint

To interact with the Llama model, make a POST request to `http://127.0.0.1:3000/llama/invoke` with the following JSON body:

```json
{
    "input": {
        "system_message": "You are a helpful assistant",
        "user_message": "Generate a list of 5 funny dog names",
        "max_tokens": 1000
    }
}
```

## Note

This project uses `llama.cpp` for CPU-only execution. Ensure that the Llama model is downloaded and added to the project folder.

## License

[MIT](https://choosealicense.com/licenses/mit/)




