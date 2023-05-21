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

1. 将 `urls.txt` 放入 `infrc.exe` 同目录中，双击 `infrc.exe` 直接运行。

2. 或者，将目录加入环境变量中，在终端中输入：

```bash
infrc [文件地址]
```

此时，文件名不一定需是 `urls.txt` 。

3. 或者，在同目录下的 `config.json` 中配置文件地址：

```json
{
    "urls": "urls.txt"
}
```

此时，文件名也不一定需是 `urls.txt` 。

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
