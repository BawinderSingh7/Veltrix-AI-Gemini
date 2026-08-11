# Configuration file for Project
import os
from dotenv import load_dotenv
from google import genai
from elevenlabs import ElevenLabs

# Load Environment
load_dotenv()

# Read API Keys
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
ELEVENLABS_API_KEY=os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_AGENT_ID=os.getenv("ELEVENLABS_AGENT_ID")
ELEVENLABS_PHONE_NUMBER_ID=os.getenv("ELEVENLABS_PHONE_NUMBER_ID")
MONGODB_USERNAME=os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD=os.getenv("MONGODB_PASSWORD")
MONGODB_CLUSTER=os.getenv("MONGODB_CLUSTER")
MONGODB_URI=f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER}"
DB_NAME='Training'

# Initialize the Clients
gemini_client = genai.Client(api_key=GEMINI_API_KEY)
elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)