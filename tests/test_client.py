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

    def test_stream_story_with_reasoning(self):
        print( "\n\n\n ----- ----- ----- ----- \n Starting test_stream_story_with_reasoning");
        client = OllamaClient()

        messages = []
        model = "deepseek-r1:14b"
        prompt = "What is 2+3"
        messages.append({"role": "user", "content": prompt})
        full_response = { "reasoning": "", "answer": ""}
        print( f"\t use model [{model}] for prompt: {prompt}");

        last_chunk_type = ""

        for chunk in client.stream_completion_with_reasoning(messages, model):
            # Process the streamed chunk, e.g., display it in a UI element
            if ( chunk["type"] == "final"):
                print("\n\n\n GOT THE FINAL CHUNK")
                full_response["reasoning"] = chunk["reasoning"]
                full_response["answer"] = chunk["answer"]
                break;
            elif (chunk["type"] != last_chunk_type):
                last_chunk_type = chunk["type"]
                print(f"\n----- {last_chunk_type}")
            chunk_new_text = chunk[last_chunk_type]
            print(f"{chunk_new_text}", end="", flush=True)

        messages.append({"role": "assistant", "content": full_response})
        print("\n\n\n\n----- ----- Full Response");
        print(full_response);        

# # Run unit test from console as follows
# # python -m unittest tests/test_client.py
