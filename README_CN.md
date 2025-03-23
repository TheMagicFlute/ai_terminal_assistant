### AI 终端助手

#### 功能特点

- **命令助手**：不再需要记住所有的终端命令，只需向 AI 提问，它会提供正确的命令。  
- **系统兼容**：AI 了解你的系统环境，提供适合你的命令。  
- **目录分析**：AI 了解你的当前目录，并能进行分析和操作建议。  

---

#### 安装方法

1. 克隆本仓库：
   ```bash
   git clone https://github.com/mengqinlol/ai_terminal_assistant.git
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 生成可执行文件：
   ```bash
   pyinstaller --onefile --name ai main.py
   ```
4. **或者，你可以直接下载 [ai.exe](https://github.com/mengqinlol/ai_terminal_assistant/releases) 并使用**  
5. 将 `ai.exe` 的路径添加到环境变量 `PATH`  
6. **首次运行 `ai` 进行初始化**
7. 按照 `ai` 提示的信息填写配置文件  

##### 如果你想使用 Ollama
- `base_url` 设为 `http://127.0.0.1:11434/v1`  
- `api_key` 不需要填写  
- `model` 可以是你已经下载的任何 Ollama 模型  
- **注意**：如果 Ollama 长时间未接收请求，首次响应可能会较慢（因为需要初始化模型）  

---

#### 使用方法

```bash
ai <你的需求>
```

示例：

```bash
(ollama) PS D:\ai_terminal> ai 查看当前目录下所有文件大小
dir /a-d /o-s
Copy(c)/ Execute(e)/ Quit(q):
```

```bash
(ollama) PS D:\ai_terminal> ai 根据这个目录创建一个叫 abc 的 Docker 镜像
docker build -t abc .
Copy(c)/ Execute(e)/ Quit(q):
```

---

#### 未来计划（TODO）

- [x] 支持 Ollama  
- [ ] 增加更多命令支持  
- [ ] 增加多语言支持  
- [ ] 支持更多操作系统  

---

#### 特别感谢

- [Ollama](https://github.com/llama-ai/llama)  
- [Python](https://www.python.org/)  
- [VSCode](https://code.visualstudio.com/)  
- [GitHub](https://github.com/)  