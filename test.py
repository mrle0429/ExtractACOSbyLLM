from openai import OpenAI
import httpx

client = OpenAI(
    base_url="https://api.gpts.vin/v1",
    api_key="sk-ECtsvUIfbBtt9mh375Bb32C57065434aAcCcE70d1fFaD24c",
    http_client=httpx.Client(
        base_url="https://api.gpts.vin/v1",
        follow_redirects=True,
    ),
)
completion = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message.content)