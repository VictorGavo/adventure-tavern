import openai

response = openai.Image.create(
  prompt="a magical ancient pangolin made of exotic materials",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']