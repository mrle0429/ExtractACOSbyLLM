import json
import random

input_text = "/mnt/SSD1/ljr2/data/Office_Products_5.json"       #针对不同数据集需要更改文件名称
input_simple_path = "output/input_simple_Office_Products_5.txt"

# 初始化抽样列表
sampled_reviews = []
with open(input_simple_path, "w") as input_simple_file:
    input_simple_file.write("")

# 打开输入文件，逐行读取数据并抽样
with open(input_text, "r") as input_file:
    for line_number, line in enumerate(input_file, start = 1):
        review_info = json.loads(line)
        sampled_reviews.append((line_number, review_info))

# 从抽样列表中随机选择十条数据
random_sample = random.sample(sampled_reviews, 10)

# 将抽样结果写入简化后的输出文件
with open(input_simple_path, "a") as input_simple_file:
    for line_number, review_info in random_sample:
        review_text = review_info.get("reviewText", "")
        summary = review_info.get("summary", "")
        main_info = f"reviewNum:{line_number}. review: {review_text}; {summary}"
        input_simple_file.write(main_info + "\n")