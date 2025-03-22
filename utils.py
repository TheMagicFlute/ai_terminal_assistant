import json
import os

from config import global_config

def process_response(ans):
    if "```" not in ans:
        return ans
    ans = ans.split('\n')
    flag = False
    res = ""
    for line in ans:
        if '```' in line and not flag:
            flag = not flag
            continue
        elif '```' in line and flag:
            flag = not flag
            break
        if flag:
            res += line + "\n"
    res = res.strip()
    return res

def process_arg(argvs):
    if len(argvs) < 2:
        print("Usage: \n\tset_model [model]\n\tset_base_url [base_url]\n\tset_api_key [api_key]\n\tafter configuration, you can just tell me what you want to do")
        return "", False
    if argvs[1] == "help":
        return "Usage: \n\tset_model [model]\n\tset_base_url [base_url]\n\tset_api_key [api_key]", False
    elif argvs[1] == "set_model":
        global_config.set_model(argvs[2])
        return "Model set to " + argvs[2], False
    elif argvs[1] == "set_base_url":
        global_config.set_base_url(argvs[2])
        return "Base URL set to " + argvs[2], False
    elif argvs[1] == "set_api_key":
        global_config.set_api_key(argvs[2])
        return "api_key set to " + argvs[2], False
    prompt = ""
    if len(argvs) > 1:
        prompt = ' '.join(argvs)
    else:
        print("没有传入参数")
    
    if ".py" in prompt.split(" ")[0] or ".exe" in prompt.split(" ")[0]:
        prompt = " ".join(prompt.split(" ")[1:])
    return prompt, True