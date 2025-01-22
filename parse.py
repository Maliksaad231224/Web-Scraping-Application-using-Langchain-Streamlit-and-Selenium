import subprocess
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Function to install Ollama CLI and download the model
def install_ollama_model():
    try:
        # Install Ollama (if not already installed)
        subprocess.run(["curl", "-s", "https://ollama.com/download.sh", "|", "bash"], check=True)
        # Download the specific Ollama model, e.g., "gemma2:2b"
        subprocess.run(["ollama", "download", "gemma2:2b"], check=True)
        st.success("Ollama and the model were successfully installed.")
    except Exception as e:
        st.error(f"Failed to install Ollama or the model. Error: {e}")

# Call the installation function
install_ollama_model()

# Define your template and model
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the Ollama model (ensure the model name matches the one downloaded)
model = OllamaLLM(model="gemma2:2b")

# Function to parse content using the Ollama model
def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)

