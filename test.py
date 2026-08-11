from config import gemini_client

for model in gemini_client.models.list():
    print(model.name)