import openai
import streamlit as st

openai.api_key=(st.secrets["api"])
def bot(text):
  response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content":"You have to correct the code if there are any errors and also write the correct code."
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


def main():
  st.set_page_config(page_title="CodeRunner")
  prompt = None
  prompt = st.chat_input("Place your code here")
  if(prompt is not None):
    code = bot(prompt)
    st.text(code)

if __name__=="__main__":
  main()
