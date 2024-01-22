from django.shortcuts import render
import openai 
import requests
import os
import json
import render
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY") 



