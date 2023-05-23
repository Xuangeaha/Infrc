# Infinite Read-Count 无限阅读量 推量工具

Copyright (c) 2023 XuangeAha(轩哥啊哈OvO)

## 使用方法

将需推量的博客地址填入 `urls.txt` 中，一行一个，以 “#” 开头将作为注释被忽略。示例：

```plaintext
# Infrc (Infinite Read-Count 无限阅读量) 推量工具 By 轩哥啊哈OvO
# 将须推量的博客地址列在下方，一行一个
# 以 “#” 开头将作为注释被忽略

# Jacky
https://blog.csdn.net/2302_77743714/article/details/130468512

# 置顶
https://xuangeaha.blog.csdn.net/article/details/128531410

# 2023年5月
https://xuangeaha.blog.csdn.net/article/details/130661244
https://xuangeaha.blog.csdn.net/article/details/130660955
https://xuangeaha.blog.csdn.net/article/details/130655328

# 2023年4月
https://xuangeaha.blog.csdn.net/article/details/130441906
```

接下来，您可以：

1. 将 `urls.txt` 放入 `infrc.exe` 同目录中，双击 `infrc.exe` **直接运行**。
2. 或者，将目录加入**环境变量**中，在终端中输入：

```bash
infrc [指定文件地址]
```

此时，文件名不一定需是 `urls.txt` 。

3. 或者，在同目录下的 `config.json` 中**配置文件地址**：

```json
{
    "urls": "urls.txt"
}
```

此时，文件名也不一定需是 `urls.txt` 。

**文件地址判断依据：终端指定 > config.json配置 > 同目录下urls.txt**

您也可以在 `config.json` 中配置等待时间（默认为30-40秒）：

```json
{
    "urls": "urls.txt",
    "sleep_time": {
        "min": 30,
        "max": 40
    }
}
```

## 已支持的博客类型

| 博客类型 | 访问 | 推量 | 阅读量爬取 |
| -------- | ---- | ---- | ---------- |
| CSDN     | √   | √   | √         |
| 其他     | √   | ?    | ?          |

## 报错列表

| 编号       | 原因                                                 | 解决方案                                     |
| ---------- | ---------------------------------------------------- | -------------------------------------------- |
| [Infrc001] | 没有找到 urls.txt 或指定的文件。                     | 参考“使用方法”配置 urls.txt 位置。         |
| [Infrc002] | 请求出错：请检查 …… 中 …… 中是否存在拼写错误... | 检查 urls.txt 中网址可用性或网络连接状态。  |
| [Infrc003] | config.json 中存在填写错误。                         | 参考“使用方法”正确填写 config.json 格式。 |
