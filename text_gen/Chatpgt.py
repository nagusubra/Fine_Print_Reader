import openai
import text_gen.private as private

# set configuration for program
myconfig = private.config()

# Set the API key
openai.api_key = myconfig.get_openai_key()

# Use the GPT-3 model to generate text
prompt = '''Summariz ethis for me "Amazon.ca Return Policy:
You may return any of the following items to Amazon.ca, for any reason, for a full refund (we'll also refund the return shipping cost, if the return is a result of our error or if the item qualifies for Free Returns) within 30 days of delivery of your shipment (including gifts):

Any book in its original condition
Any unopened (still in its plastic wrap) CD, DVD, VHS tape, software, or video game
Unworn jewelry, watches, shoes, clothing and accessories (see "Returning Jewelry and Watches" and "Returning Shoes, Clothing & Accessories" below for more details)
You may return eligible baby items and toys to Amazon.ca, for any reason, for a full refund (we'll also refund the return shipping cost, if the return is a result of our error) within 45 days of delivery of your shipment (including gifts). Also, most health and personal care items can be returned within 60 days of delivery (subject to the exclusions below).

Please note that we cannot accept the return of opened items, some health and personal care items, grocery items, or items returned more than 30 days past delivery (45 days for eligible baby items and toys; 60 days for eligible health and personal care items). We can only process returns and refunds for items purchased at Amazon.ca.

If you ordered your item from an Amazon Marketplace seller, please see our Marketplace returns policy for more information about returning your order."
'''



model = "text-davinci-002"
completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=2048, n=1,stop=None,temperature=0.45)
message = completions.choices[0].text
print(message)




# response = openai.Image.create(
#   prompt="quirky instagram profile picture",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']
