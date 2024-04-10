"""7-Zip Utility script."""

# Standard Library
import os
import subprocess

# 3rd party Libarary

# Define Global Constant

# Define Global Variable


# Define Function
def compress_7zip(src_dir, compress_file):
    """Compress."""
    # Refer Global Variable

    # Define Local Constant
    NORMAL = 0
    ERROR = 1
    TARGET_FILE_EXTENSION = "*"  # *.txt *.log"

    # Define Local Variable
    return_code = ERROR
    toolpath_7zip = ""

    print("\n-----Start compress-----\n")

    # Install check 7-zip
    toolpath_7zip = install_check_7zip()

    if toolpath_7zip != "":
        # ↓スペースのsplitではC:/Program Files部分を認識できないため直接コマンドを指定
        # cmd = toolpath_7zip + " a " + compress_file + " " + src_dir + " -r " + TARGET_FILE_EXTENSION
        # result = subprocess.run(cmd.split())
        result = subprocess.run(toolpath_7zip + " a " + compress_file + " " + src_dir + " -r " + TARGET_FILE_EXTENSION)
        return_code = result.returncode

        if return_code == NORMAL:
            print("OK:Successed compress.")
        else:
            print("Error:Failed compress.")

    print("\n-----End compress-----\n")


def extract_7zip(src_file, extract_dir):
    """extract."""
    # Refer Global Variable

    # Define Local Constant
    NORMAL = 0
    ERROR = 1
    TARGET_FILE_EXTENSION = "*"  # *.txt *.log"

    # Define Local Variable
    return_code = ERROR
    toolpath_7zip = ""

    print("\n-----Start extract-----\n")

    # Install check 7-zip
    toolpath_7zip = install_check_7zip()

    if toolpath_7zip != "":
        # ↓スペースのsplitではC:/Program Files部分を認識できないため直接コマンドを指定
        # cmd = toolpath_7zip + " x " + src_file + " -o " + extract_dir + " -r " + TARGET_FILE_EXTENSION
        # result = subprocess.run(cmd.split())
        result = subprocess.run(toolpath_7zip + " x " + src_file + " -o" + extract_dir + " -r " + TARGET_FILE_EXTENSION)
        return_code = result.returncode

        if return_code == NORMAL:
            print("OK:Successed extract.")
        else:
            print("Error:Failed extract.")

    print("\n-----End extract-----\n")


def install_check_7zip():
    """Install check 7-zip."""
    # Refer Global Variable

    # Define Local Constant
    TOOLPATH_X86_7ZIP = "C:/Program Files (x86)/7-Zip/7z.exe"
    TOOLPATH_X64_7ZIP = "C:/Program Files/7-Zip/7z.exe"

    # Define Local Variable
    toolpath_7zip = ""

    print("\n-----Start install check 7-zip-----\n")

    # 7-zipアプリケーションの設定
    if os.path.isfile(TOOLPATH_X86_7ZIP) is True:
        toolpath_7zip = TOOLPATH_X86_7ZIP
    elif os.path.isfile(TOOLPATH_X64_7ZIP) is True:
        toolpath_7zip = TOOLPATH_X64_7ZIP
    else:
        toolpath_7zip = ""

    if toolpath_7zip != "":
        print("OK:Successed 7-zip install check.")
    else:
        print("Error:Failed 7-zip install check.")
        print("Not found 7-zip appication.")
        print("Please install 7-zip.")

    print("\n-----End install check 7-zip-----\n")
    return toolpath_7zip


# if __name__ == "__main__":
    # compress_7zip(src_dir="", compress_file="")
    # extract_7zip(src_file="", extract_dir="")
