import openai
from pydantic import BaseModel

import argparse
import platform
import os
import sys
import pyperclip

import env

SYS = platform.system()
TERMINAL = ""

# 在 Windows 上，cmd.exe 或 PowerShell 由 COMSPEC 变量决定
if os.name == "nt":
    TERMINAL = os.environ.get("COMSPEC", "未知终端")  # 通常是 cmd.exe 或 powershell.exe
else:
    # 在 Linux/macOS 上，SHELL 变量存储了终端信息
    TERMINAL = os.environ.get("SHELL", "未知终端")  # 通常是 /bin/bash 或 /bin/zsh


if __name__ == "__main__":

    client = openai.OpenAI(
        base_url=env.BASE_URL,  # Ollama 本地 API
        api_key=env.API_KEY,  # Ollama API Key"  # 这个 key 可以随便填，Ollama 不需要鉴权
    )

    if len(sys.argv) > 1:
        prompt = ' '.join(sys.argv)
    else:
        print("没有传入参数")
    
    if ".py" in prompt.split(" ")[0] or ".exe" in prompt.split(" ")[0]:
        prompt = " ".join(prompt.split(" ")[1:])

    print(prompt)

    response = client.chat.completions.create(
    model=env.MODEL,
    messages=[
        {
            "role": "system",
            "content": f"""你是计算机领域的专家，用户在用的系统是 {SYS}，终端是 {TERMINAL}，
            这是用户当前目录下的文件列表：{os.listdir()}，用户当前目录是：{os.getcwd()}，
            用户将提出一个关于终端命令的问题，请直接帮他写出对应的命令，直接写出！不要解释，不要解释，不要解释，直接输出命令，不要输出多个命令，不要 markdown 格式!!
            """
        },
        {
            "role": "user",
            "content": prompt,
        }
    ],
    temperature=0
)

    print(response.choices[0].message.content)

    res = input("复制(c)/ 执行(e)/ 退出(q):")

    if res == "c":
        pyperclip.copy(response.choices[0].message.content)
    elif res == "e":
        os.system(response.choices[0].message.content)