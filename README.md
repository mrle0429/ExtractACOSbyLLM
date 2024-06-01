# ChatGPT提取评论中的四元组
## 参考文章
- Xu, X., Zhang, J. D., Xiao, R., & Xiong, L. (2023). The Limits of ChatGPT in Extracting Aspect-Category-Opinion-Sentiment Quadruples: A Comparative Analysis. arXiv preprint arXiv:2310.06502.
- Kim, J., Heo, R., Seo, Y., Kang, S., Yeo, J., & Lee, D. (2024). Self-Consistent Reasoning-based Aspect-Sentiment Quad Prediction with Extract-Then-Assign Strategy. arXiv preprint arXiv:2403.00354.


# 提取方面术语-方面类别-意见术语-情感极性
隐式方面术语/意见术语 -> NULL

类别和情感不能为空

# 提示词模板设计思路
- 固定的提示(指令)
- 输出格式
- 预设方面类别（不是唯一）
- 预设情感极性[Positive, Negative, Neutral]
- 示例：
    - Input:
    - Output:
    - Reasoning:

```text
I am performing the ASQP task, which is the Subtask of ABSA (Aspect-Based Sentiment Analysis). 
Instruction: Extract aspect-category-opinion-sentiment quadruples from input data according to the following guidelines: 
1. An aspect term or opinion term must be a phrase present in the input sentence or NULL if it is not explicitly mentioned.
2. The aspect term/opinion term can be NULL, representing implicit expressions.
3. The category must be inferred based on the aspect term and opinion term. The category is one in the predefined list. 
However, there can also be other aspect category collections. You can infer that for yourself
4. Sentiment polarity must be judged comprehensively considering the context of the sentence.
5. Sentiment polarity should be one of the following: [’positive’, ’neutral’, ’negative’].
6. Do not ask for more information, just try your best to complete the task.

Output format: (aspect, category, opinion, sentiment)

Possible aspect category set: 

You can learn from the following examples.

[Example 1]
Input: The fried dumplings are GREAT!
Output: (’fried dumplings’, ’food quality’, ’GREAT’, ’positive’)
Reasoning: In this sentence, the aspect term is ‘fried dumplings’ and the opinion term for this aspect term is
‘GREAT’. Since the aspect term is ‘fried dumplings’ and the opinion about the aspect term is ‘GREAT’, the
aspect category can be inferred as ‘food quality’ for this aspect term. Lastly, the aspect term ‘fried dumplings’
is evaluated as a opinion of ‘GREAT’. When it comes to food, the opinion ’GREAT’ suggests that the food is
delicious, which is evaluated as a positive sentiment
```


## 项目结构
### 目录结构
```text
ExtractACOSbyLLM/
├── Output/               # 存放中间过程输出和最终提取结果输出
├── promoting_txt/        # 存放提示词文本
├── main.py               # 从评论中提取方面类别的主程序
├── data_loader.py        # 数据加载和预处理模块
└── test.py               # 用于测试API是否正常调用
```


### 环境配置
**不一定可用**

环境放置在 ```openai-env/Scripts/python.exe```

1. 打开项目文件夹
2. 找到 File | Settings | Project: ExtractACOSbyLLM | Python Interpreter
3. Add Interpreter -> Local -> Existing 使用```openai-env/Scripts/python.exe```
4. Apply -> OK
5. Run右侧的三个点。选择运行的环境

### 模块说明
**data_loader**
该模块用于加载和预处理评论数据。

- `load_data(file_path)`: 加载指定路径的JSON文件。
- `simplify_data(data)`: 简化JSON数据，提取 reviewNum, reviewText, summary。
- `random_sample(data, sample_size)`: 从简化后的数据中随机抽样。

**main.py**
该模块是从评论中提取方面类别的主程序。

- `extract_acos(review_text)`: 根据提供的提示词模板，从评论文本中提取方面-类别-意见-情感四元组。
- `load_data('reviews.json')`: 加载评论数据。
- `simplify_data(data)`: 简化数据。
- `random_sample(simplified_data, 5)`: 随机抽取5条评论。
- 对每条评论调用 `extract_acos(review_text)` 并打印结果。

**test.py**
该模块用于测试API是否正常调用。
