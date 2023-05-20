# Infinite Read-Count 无限阅读量 推量工具 By 轩哥啊哈OvO

Copyright (c) 2023 XuangeAha(轩哥啊哈OvO)

## 使用方法

将需推量的博客地址填入`urls.txt`放入`infrc.exe`同目录中，一行一个，以 “#” 开头将作为注释被忽略。双击`infrc.exe`运行。示例：

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

可在同目录下的`config.json`中配置等待时间（默认为30-40秒）：

```json
{
    "sleep_time": {
        "min": 30,
        "max": 40
    }
}

```
