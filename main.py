import openai

openai.api_key=("paste your api key")
def bot(text):
  response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content":"debug the given code."
            },
            {
                "role": "user",
                "content":text
            }
          ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
  generated_text=response.choices[0].message.content.strip()
  return generated_text


     
