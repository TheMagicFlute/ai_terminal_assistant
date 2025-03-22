import openai
from pydantic import BaseModel

import argparse
import platform
import os
import sys
import pyperclip

from utils import *

SYS = platform.system()
TERMINAL = ""

# 在 Windows 上，cmd.exe 或 PowerShell 由 COMSPEC 变量决定
if os.name == "nt":
    TERMINAL = os.environ.get("COMSPEC", "未知终端")  # 通常是 cmd.exe 或 powershell.exe
else:
    # 在 Linux/macOS 上，SHELL 变量存储了终端信息
    TERMINAL = os.environ.get("SHELL", "未知终端")  # 通常是 /bin/bash 或 /bin/zsh


if __name__ == "__main__":
    prompt, res = process_arg(sys.argv)
    if not res:
        print(prompt)
        sys.exit()
    config = global_config.get_config()
    client = openai.OpenAI(
        base_url=config["base_url"],  # Ollama 本地 API
        api_key=config["api_key"],  # Ollama API Key"  # 这个 key 可以随便填，Ollama 不需要鉴权
    )
    files = [item for item in os.listdir() if not item.startswith('.')]
    response = client.chat.completions.create(
    model=config["model"],
    messages=[
        {
            "role": "system",
            "content": f"""你是计算机领域的专家，用户在用的系统是 {SYS}，终端是 {TERMINAL}，
            用户将提出一个关于终端命令的问题，请直接帮他写出对应的命令，直接写出！不要解释，不要解释，不要解释，直接输出命令，不要输出多个命令，不要 markdown 格式!!
            """
        },
        {
            "role": "user",
            "content": f'''我现在在{SYS}系统的{TERMINAL} 终端下，我所在的目录是{os.getcwd()}，该目录下有这些文件{files}
            我想执行 {prompt}''',
        }
    ],
    temperature=0
    )

    ans = response.choices[0].message.content
    ans = process_response(ans)

    print(ans)

    res = input("复制(c)/ 执行(e)/ 退出(q):")

    if res == "c":
        pyperclip.copy(ans)
    elif res == "e":
        os.system(ans)