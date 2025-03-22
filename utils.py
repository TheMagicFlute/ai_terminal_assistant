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

def get_all_executable_commands():
    executables = set()
    path_dirs = os.environ.get('PATH', '').split(os.pathsep)
    
    # 获取系统支持的可执行文件扩展名（Windows 特有）
    if os.name == 'nt':
        pathext = os.environ.get('PATHEXT', '.exe;.bat;.cmd').lower().split(';')
        valid_extensions = {ext.lower() for ext in pathext}
    else:
        valid_extensions = None  # 非 Windows 不检查扩展名

    for dir_path in path_dirs:
        if not os.path.isdir(dir_path):
            continue

        try:
            with os.scandir(dir_path) as it:
                for entry in it:
                    # 仅处理文件或符号链接（排除目录）
                    if not (entry.is_file() or entry.is_symlink()):
                        continue

                    # Windows：检查扩展名是否在 PATHEXT 中
                    if os.name == 'nt':
                        _, ext = os.path.splitext(entry.name)
                        if ext.lower() not in valid_extensions:
                            continue  # 跳过无效扩展名

                    # 检查文件是否可执行
                    if os.access(entry.path, os.X_OK):
                        # 提取命令名称（Windows 去掉扩展名，其他系统保留原名）
                        if os.name == 'nt':
                            cmd_name = entry.name
                            for ext in valid_extensions:
                                if cmd_name.lower().endswith(ext):
                                    cmd_name = cmd_name[:-len(ext)] if ext else cmd_name
                                    break
                        else:
                            cmd_name = entry.name

                        executables.add(cmd_name)
        except PermissionError:
            continue

    return sorted(executables)

if __name__ == "__main__":
    # 获取并打印所有可执行命令
    all_commands = get_all_executable_commands()
    print("可用命令列表：")
    print('\n'.join(all_commands))