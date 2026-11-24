from ollama import Client
 
MODEL = 'qwen3.5:4b'  # Replace after: ollama list
client = Client(host='http://localhost:11434')
 
verified = {'title': 'AI Handbook', 'price_myr': 40.0,
            'stock': 12}
request = ('Write one concise sentence using only these '
           f'verified facts: {verified}. Do not invent details.')
 
try:
    result = client.chat(
        model=MODEL,
        messages=[{'role': 'user', 'content': request}]
    )
    print(result.message.content)
except Exception as error:
    print('Local model request failed:', error)

