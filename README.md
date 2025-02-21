# ollama_lib

A simple python library to work with locally hosted Ollama.

## Preparation

Ollama makes it easy to host wide range of LLMs.
Both the raw LLM models and modelfiles (with system prompts) can be loaded.

See [SHAIL with Ollama](https://github.com/funmu/shail) for self hosting with Ollama.
Once installed, Ollama runs at <http://localhost:11434/>.
Access the APIs at **/api/generate** endpoint. It supports both full and chunked response.

## Ollama_lib

*Ollama_lib* encapsulates the calls to Ollama endpoint and gives 2 simple methods

1. *generate_text(prompt, model_id)* - Generates text based on model and given prompt.
2. *stream_completion(messages, model_id)* - Streams a chat completion from an Ollama-hosted LLM.

See [ollama_lib code](./ollama_lib/) for details.

```text

class OllamaClient(builtins.object)
 |  OllamaClient(api_base='http://localhost:11434')
 |
 |  Methods defined here:
 |
 |  __init__(self, api_base='http://localhost:11434')
 |      Initializes the OllamaClient.
 |
 |      :param str api_base: The base URL of the Ollama API.
 |
 |  generate_text(self, prompt, model_id)
 |      Generates text using an Ollama-hosted LLM.
 |
 |      :param str prompt: The prompt to send to the LLM.
 |      :param str model_id: The ID of the LLM model to use.
 |      :returns: The generated text response.
 |      :rtype: str
 |
 |  stream_completion(self, messages, model_id)
 |      Streams a chat completion from an Ollama-hosted LLM.
 |
 |      :param list messages: A list of messages in the chat history.
 |      :param str model_id: The ID of the LLM model to use.
 |
 |      :yields: Chunks of the generated text response.
 |      :ytype: str
```

## Testing Ollama_lib

See [Test ollama_lib](./tests/) for the tests included to call and use the methods.

You can run the tests using python's **unittest** module.

```sh
# run the unit tests defined in the test_client.py
python -m unittest tests/test_client.py

# you can also run the tests from the run_tests.py

python run_tests.py
```

## Install Module

Install this ollama_lib module locally using

```sh
# create a local intance of the Ollama_lib module
pip install -e.
```

NOTE: Need to upgrade this locally intallable package to use pyproject.toml and new pip manager.
