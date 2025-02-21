import requests
import json

class OllamaClient:
    def __init__(self, api_base="http://localhost:11434"):
        """Initializes the OllamaClient.

      :param str api_base: The base URL of the Ollama API.
        """
        self.api_base = api_base
        self.isVerbose = False

    def generate_text(self, prompt, model_id):
        """Generates text using an Ollama-hosted LLM.

        :param str prompt: The prompt to send to the LLM.
        :param str model_id: The ID of the LLM model to use.
        :returns: The generated text response.
        :rtype: str
        """
        url = f"{self.api_base}/api/generate"
        headers = {"Content-Type": "application/json"}
        data = {"model": model_id, "stream": False, "prompt": prompt}
        formattedData= json.dumps(data);

        if (self.isVerbose):
            print( f" headers: {headers}\ndata: {formattedData}");

        try:
            response = requests.post(url, headers=headers, data=formattedData)
            if (self.isVerbose):
                print( f" raw response is:");
                print(response);
            response.raise_for_status()  # Raise an exception for bad status codes
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            if response.status_code == 400:  # Bad Request
                try:
                    error_message = response.json().get("error", "")
                    print(f"Ollama API Error: {error_message}")
                except ValueError:
                    print("Invalid JSON error response from Ollama API.")
                exit(1);

        response_json = response.json()
        return response_json.get("response", "")

    def stream_completion(self, messages, model_id, context_window=8000):
        """Streams a chat completion from an Ollama-hosted LLM.

        :param list messages: A list of messages in the chat history.
        :param str model_id: The ID of the LLM model to use.
        :param int context_window: Number of tokens in the context window.

        :yields: Chunks of the generated text response.
        :ytype: str
        """
        url = f"{self.api_base}/api/generate"
        headers = {"Content-Type": "application/json"}
        data = {"model": model_id, 
            "stream": True, # Enable streaming 
            "options": {"num_ctx": context_window},
            "prompt": ""}  

        # Format messages into a single string
        formatted_messages = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
        data["prompt"] = formatted_messages
        formattedData= json.dumps(data);

        if (self.isVerbose):
            print( f" headers: {headers}\ndata: {formattedData}");

        try:
            response = requests.post(url, headers=headers, data=formattedData, stream=True)
            if (self.isVerbose):
                print( f" raw response is:");
                print(response);
            response.raise_for_status()  # Raise an exception for bad status codes
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            if response.status_code == 400:  # Bad Request
                try:
                    error_message = response.json().get("error", "")
                    print(f"Ollama API Error: {error_message}")
                except ValueError:
                    print("Invalid JSON error response from Ollama API.")
                exit(1);

        for chunk in response.iter_lines():
            if chunk:
                try:
                    decoded_chunk = chunk.decode("utf-8")
                    response_json = json.loads(decoded_chunk)
                    generated_text = response_json.get("response", "")
                    yield generated_text
                except json.JSONDecodeError:
                    print(f"Error decoding JSON chunk: {chunk}")
