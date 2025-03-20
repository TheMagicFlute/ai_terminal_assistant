## AI_TERMINAL_ASSISTANT

### A simple AI terminal command line assistant

#### Installation

1. Clone the repository
2. Install the requirements
3. Fill in your BASE_URL, API_KEY, MODEL in the env.py file (if you`re using ollama, the default BASE_URL is http://localhost:11434/v1, and API_KEY is not nesscary)
4. Pyinstaller --onefile main.py
5. Rename the output file to ai.exe
6. Add ai.exe to your PATH

#### Usage

``` bash
ai <Your need>
```

Examples:

``` bash
(ollama) PS D:\ai_terminal> ai 查看当前目录下所有文件大小
查看当前目录下所有文件大小
dir /a /s /q
复制(c)/ 执行(e)/ 退出(q):e
 驱动器 D 中的卷是 新加卷
 卷的序列号是 6E53-47A5

 D:\ai_terminal 的目录
 ...
```


```
(ollama) PS D:\ai_terminal> ai 根据这个目录创建一个叫abc的docker
根据这个目录创建一个叫abc的docker
docker build -t abc .
复制(c)/ 执行(e)/ 退出(q):
```