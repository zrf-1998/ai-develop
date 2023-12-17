---
title: ai-dev
date: 2023-12-17 15:45:02
type: 
updated: 
categories: 
tags: 
    - 
    - 
description: 
cover: 
---

## 一. 配置python环境

```bash
# 创建虚拟环境d
zrf@debian:~/git/ai-develop$ python3 -m venv ai-dev

# 激活环境
zrf@debian:~/git/ai-develop$ source ai-dev/bin/activate
(ai-dev) zrf@debian:~/git/ai-develop$ 

# 安装Python 库
(ai-dev) zrf@debian:~/git/ai-evelop$ pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 二. 配置本地APIKEY

```bash
# 添加自己的APIKEY
(ai-dev) zrf@debian:~/git/ai-develop$ cat .env 
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
OPENAI_API_KEY=abc123

# 如果你的KEY需要代理的话需要配置以下环境变量
OPENAI_API_BASE_URL=

# 配置环境变量
(ai-dev) zrf@debian:~/git/ai-develop$ source .env 

# 测试环境变量
(ai-dev) zrf@debian:~/git/ai-develop$ echo $OPENAI_API_KEY
abc123
```
