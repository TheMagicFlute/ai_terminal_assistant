## AI_TERMINAL_ASSISTANT

### A simple AI terminal command line assistant

#### Installation

1. Clone the repository
2. Install the requirements
3. `pyinstaller --onefile --name ai main.py`
4. Rename the output file to ai.exe
5. OR YOU CAN JUST DOWNLOAD THE [ai.exe](https://github.com/mengqinlol/ai_terminal_assistant/releases) FROM release
6. Add path to the ai.exe to your PATH
7. First, run `ai` in your terminal for initialization.
8. Then, follow the instuction given by `ai` to fill in your configration

##### If you want to use Ollama
- `base_url` should be `http://127.0.0.1:11434/v1`
- 'api_key' is not needed
- 'model' can be any model you`ve pulled from ollama
- IT SHOULD BE noted that Ollama may take a long time to process your request if it hasn't received any requests for a while, due to the initialization of the model.


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
