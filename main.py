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


def extract_quadruples(text, dataset_name):
    with open(dataset_name, "r") as file:
        prompt_text = file.read()

    completion = client.chat.completions.create(
        seed=123456,
    model="gpt-4-1106-preview",
    messages=[
        {
            "role": "system",
            "content": prompt_text
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
dataset_name = "Automotive_5"   # 需要修改数据集名称
input_text = f"output/input_simple_{dataset_name}.txt"   #针对不同数据集需要更改文件名称
output_text = f"output/output_{dataset_name}.txt"   # 需要修改文件名
with open(output_text, "w") as output_file:
    output_file.write("")


with open(input_text, "r") as input_file:

    for line in input_file:
        review_number, review = line.strip().split(" ", 1)
        review_number = str(review_number)
        result = str(extract_quadruples(review, f"promoting_txt/{dataset_name=}.txt"))

        with open(output_text, "a") as output_file:
            output_file.write(str(review_number) + " " + result + "\n")

