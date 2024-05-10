import json

from openai import OpenAI
import httpx

client = OpenAI(
    base_url="https://api.xiaoai.plus/v1",
    api_key="sk-mGRD5KEwL1Of139057C117B82f0343729dC264E34c7578Cd",
    http_client=httpx.Client(
        base_url="https://api.xiaoai.plus/v1",
        follow_redirects=True,
    ),
)

promoting_Grocery_and_Gourmet_Food_5 = '''
I am performing the ASQP task, which is the Subtask of ABSA. 
Instruction: extract aspect-category-opinion-sentiment quadruples from input data. 
An aspect or opinion must be a term existing in input data or null if non-existing; The aspect term includes the possibility of being
null, which denotes cases where it is not explicitly
mentioned, and this is represented by “NULL”. 
From now on, if I give you a sentence, create the quadruples according to reason. 
Please just output the ASQP. Output format neet to follow (aspect, category, opinion, sentiment). 
When extracting aspect term and option term, an aspect category is judged by a combination of aspect term and opinion term, and sentimental polarity is judged by comprehensively
considering everything.
Here are possible aspect category set: [’food prices’, ’food style_options’, ’service general’, ’drinks prices’, ’am-
bience general’, ’drinks quality’, ’location general’, ’restaurant prices’, ’restaurant general’, ’drinks style_options’,
’food general’, ’restaurant miscellaneous’, ’food quality’].
Here are possible sentiment polarity set: [’positive’,’negative’,’neutral’].
do not ask me for more information, I am unable to
provide it, and just try your best to finish the task.
You can learn from the following examples.
[Example 1]
Input: The fried dumplings are GREAT!
Output: [’fried dumplings’, ’food quality’, ’GREAT’, ’positive’]
Reasoning: In this sentence, the aspect term is ‘fried dumplings’ and the opinion term for this aspect term is
‘GREAT’. Since the aspect term is ‘fried dumplings’ and the opinion about the aspect term is ‘GREAT’, the
aspect category can be inferred as ‘food quality’ for this aspect term. Lastly, the aspect term ‘fried dumplings’
is evaluated as a opinion of ‘GREAT’. When it comes to food, the opinion ’GREAT’ suggests that the food is
delicious, which is evaluated as a positive sentiment
[Example 2]
Input: It’s one of our favorite places to eat in NY.
Output: [’NULL’, ’restaurant general’, ’positive’, ’favorite’]
Reasoning: In this sentence, there is no specific aspect term mentioned explicitly. So the aspect term is ‘NULL’
and the opinion term for this aspect term is ‘favorite’. The aspect category could be inferred as ’restaurant
general’ as the speaker is expressing a general sentiment about the restaurant rather than a specific feature or
component. Lastly, by referring to the restaurant as a ’favorite’, the speaker implies a positive sentiment polarity.
'''
promoting_Musical_Instruments_5 = '''
 am performing the ASQP task, which is the Subtask of ABSA. 
Instruction: extract aspect-category-opinion-sentiment quadruples from input data. The input data are comments given by users after purchasing Musical Instruments.
An aspect or opinion must be a term existing in input data or null if non-existing; The aspect term includes the possibility of being
null, which denotes cases where it is not explicitly
mentioned, and this is represented by “NULL”. 
From now on, if I give you a sentence, create the quadruples according to reason. 
Please just output the ASQP. Output format neet to follow (aspect, category, opinion, sentiment). 
When extracting aspect term and option term, an aspect category is judged by a combination of aspect term and opinion term, and sentimental polarity is judged by comprehensively
considering everything.
Here are possible aspect category set: ['sound quality', 'durability', 'price/value', 'ease of use', 'brand reputation', 'aesthetic design', 'overall performance'].
There can also be other aspect category collections. You can infer that for yourself.
Here are possible sentiment polarity set: [’positive’,’negative’,’neutral’].
Do not ask me for more information, I am unable to
provide it, and just try your best to finish the task.
You can learn from the following examples.
[Example 1]
Input: "I still operate in an analog environment quite often, so I end up using lots of inserts. I have 8 channels of compression, limiter, gate and expander, plus various EQs and effects processors that need to be routed and applied to specific channels. I have an insert snake that I use as well, but the individual insert cables (of differing lengths) that I carry are lifesavers that make me a more efficient soundman during setup and a more flexible soundman during the show!",  "Soundman must have insert cables"
Output: ['insert cables', 'overall perfermance', 'efficient', 'positive']
Reasoning: In this sentence, the aspect term is ‘insert cables’ and the opinion term for this aspect term is
‘efficient’. Since the aspect term is ‘insert cables’ and the opinion about the aspect term is ‘efficient’, the
aspect category can be inferred as ‘overall perfermance’ for this aspect term. Lastly, the aspect term ‘insert cables’
is evaluated as a opinion of ‘efficient’. When it comes to perfermance, the opinion ’positive’ suggests that the insert cables is
useful, which is evaluated as a positive sentiment
[Example 2]
Input: "very nice guitar pics, sound almost as nice as metal guitar pics, very lovely, size was as expected, great sound", "summary": "high quality"
Output: ['sound', 'sound quality', 'great', 'positive'], ['NULL', 'aesthetic design', 'lovely', 'positive']
'''

promoting_Office_Products_5 = '''
I am performing the ASQP task, which is the Subtask of ABSA. 
Instruction: extract aspect-category-opinion-sentiment quadruples from input data. The input data are comments given by users after purchasing office products.
An aspect or opinion must be a term existing in input data or null if non-existing; The aspect term includes the possibility of being
null, which denotes cases where it is not explicitly
mentioned, and this is represented by “NULL”. 
From now on, if I give you a sentence, create the quadruples according to reasoning. 
Please just output the ASQP. Output format neet to follow (aspect, category, opinion, sentiment). 
When extracting aspect term and option term, an aspect category is judged by a combination of aspect term and opinion term, and sentimental polarity is judged by comprehensively
considering everything.
Here are possible aspect category set: [’product_quality’, ’functionality’, ’price’, ’service’, ’design’, ’deliver’, ’UE(user experience)’, ’consumables’, ’environmentally_friendly’, ’brand_effect’, 'space usage', 'installation'].
There can also be other aspect category collections. You can infer that for yourself.
Here are possible sentiment polarity set: [’positive’,’negative’,’neutral’].
do not ask me for more information, I am unable to provide it, and just try your best to finish the task.
You can learn from the following examples.
[Example 1]
Input: I have an Epson Photo Stylus 2000p and paid way more than this HP photosmart printer. They are comparable in print quality. You can print small or large and the quality is amazing. What is great about this printer is the cartridge system. If you run out of a certain color just purchase that color. That is one of the reasons I dumped the Epson printer. If you run out a certain color you have to trash the entire cartridge. Set up was a breeze on the macbook. Rather than using the cd's in the box I downloaded the latest drivers online. This is best and saves time in case you encounter a problem. Sometimes the cd's that come with the printer are already outdated. Overall I am very happy with the printer. It is a tad bit large but worth the space used. Great photo lab prints!
Output: [’paid’, ’price’, ’more than HP’, ’positive’], ['print quality', 'product_quality', 'amazing', 'positive'], ['cartridge system', 'consumables', 'great', 'positive'], ['NULL', 'installation', 'best', 'positive'], ['space used', 'space usage', 'a tad bit large', 'neutral']

[Example 2]
Input: Very comfortable office chair. A great find. Cheap and reliable. Would buy another if I needed a second office chair. Great chair.
Output: [’null’, ’product_quality’, ’comfortable’, ’positive’], ['null', 'price', 'cheap', 'positive'], ['null', 'product_quality', 'reliable', 'positive']
'''

def extract_quadruples(text):
    completion = client.chat.completions.create(
        seed=123456,
    model="gpt-4-1106-preview",
    messages=[
        {
            "role": "system",
            "content": promoting_Office_Products_5
        },
        {
            "role": "user",
            "content": text
        }
  ],
        temperature= 0.1

        
)
    
    return {
    completion.choices[0].message.content
    }

# 输入你的文本
input_text = "output/input_simple_Office_Products_5.txt"   #针对不同数据集需要更改文件名称
output_text = "output/output_Office_Products_5.txt"   # 需要修改文件名
with open(output_text, "w") as output_file:
    output_file.write("")


with open(input_text, "r") as input_file:

    for line in input_file:
        review_number, review = line.strip().split(" ", 1)
        review_number = str(review_number)
        result = str(extract_quadruples(review))

        with open(output_text, "a") as output_file:
            output_file.write(str(review_number) + " " + result + "\n")

