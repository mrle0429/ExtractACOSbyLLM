# 大模型提取评论中的四元组
## 环境配置
环境放置在 ```openai-env/Scripts/python.exe```

1. 打开项目文件夹
2. 找到 File | Settings | Project: ExtractACOSbyLLM | Python Interpreter
3. Add Interpreter -> Local -> Existing 使用```openai-env/Scripts/python.exe```
4. Apply -> OK
5. Run右侧的三个点。选择运行的环境

# 提示词模板设计思路
固定的提示话术
预设方面类别（不是唯一）
情感词
EX1
EX2
尽量给出Reasoning

# 项目思路
## 仓库架构
### Output
存放中间过程输出和最终提取结果输出

### promoting_txt
存放提示词文本

### main.py
从评论中提取方面类别的主程序

### data_loader.py
1. 随机抽样评论
2. 简化json文件，提取reviewNum,reviewText,summary.

### test.py
用于测试API是否正常调用