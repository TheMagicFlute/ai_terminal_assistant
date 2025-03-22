## AI_TERMINAL_ASSISTANT

### A simple AI terminal command line assistant

#### Installation

1. Clone the repository
2. Install the requirements
3. Pyinstaller --onefile main.py
4. Rename the output file to ai.exe
5. Add ai.exe to your PATH
6. First, run `ai` in your terminal for initialization.


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
