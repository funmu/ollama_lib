import unittest
from ollama_lib.client import OllamaClient

class TestOllamaClient(unittest.TestCase):

    def test_generate_text(self):

        print( "\n\n\n ----- ----- ----- ----- ----- ----- -----\n Starting test_generate_text");
        client = OllamaClient()
        #... add assertions to test the generate_text method...
        prompt = "Climate Change"
        model = "meme_maker"
        print( f"\t use model: [{model}] with prompt: {prompt}");
        response = client.generate_text( prompt, model)
        print(response)    

    def test_stream_story(self):
        print( "\n\n\n ----- ----- ----- ----- ----- ----- -----\n Starting test_stream_story");
        client = OllamaClient()
        #... add assertions to test the generate_text method...
        # response = client.stream_completion("Tell me a 100 word story", "deepseek-r1:14b")
        # print(response)

        messages = []
        model = "deepseek-r1:14b"
        prompt = "Tell me a story in 100 words"
        messages.append({"role": "user", "content": prompt})
        full_response = ""
        print( f"\t use model [{model}] for prompt: {prompt}");

        for chunk in client.stream_completion(messages, model):
            # Process the streamed chunk, e.g., display it in a UI element
            print(chunk, end="", flush=True)
            full_response += chunk

        messages.append({"role": "assistant", "content": full_response})
        print("\n\n\n\n----- ----- Full Response");
        print(full_response);        

# Run unit test from console as follows
# python -m unittest tests/test_client.py
