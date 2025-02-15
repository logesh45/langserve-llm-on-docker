from flask import Flask, request, jsonify
from llama_cpp import Llama

# Create a Flask object
app = Flask("Llama server")
model = None


@app.route('/llama', methods=['POST'])
def generate_response():
    global model

    try:
        data = request.get_json()

        # Check if the required fields are present in the JSON data
        if 'system_message' in data and 'user_message' in data and 'max_tokens' in data:
            system_message = data['system_message']
            user_message = data['user_message']
            max_tokens = int(data['max_tokens'])

            # Prompt creation
            prompt = f"""<s>[INST] <<SYS>>
            {system_message}
            <</SYS>>
            {user_message} [/INST]"""

            # Create the model if it was not previously created
            if model is None:
                # Put the location of to the GGUF model that you've download from HuggingFace here
                model_path = "<<your model name>>"

                # Create the model
                model = Llama(model_path=model_path)

            # Run the model
            output = model(prompt, max_tokens=max_tokens, echo=True)

            print(output)
            return jsonify(output)

        else:
            return jsonify({"error": "Missing required parameters"}), 400

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)