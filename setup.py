from setuptools import setup, find_packages

setup(
    name="ollama_lib",
    version="0.2.3",
    packages=find_packages(),
    install_requires=["requests"],  # dependencies
    #... other metadata...
)