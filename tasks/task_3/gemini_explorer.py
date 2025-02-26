import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = 'sample-gemini'
vertexai.init(project = project)

config = generative_models.GenerativeConfig(
    temperature=0.4
)
# Load model with config
model = GenerativeModel(
    "gemini-pro",
    generative_config = config
)
chat = model.start_chat()