import openai
import private

# set configuration for program
myconfig = private.config()

# Set the API key
openai.api_key = myconfig.get_openai_key()

# input
input_text =  open('input/text_files/Amazon_return_policy.txt','r').read()

# Use the GPT-3 model to generate text
prompt = 'Summarize this for me "' + input_text + '"'
model = "text-davinci-002"
completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=2048, n=1,stop=None,temperature=0.45)
message = completions.choices[0].text



print(message)