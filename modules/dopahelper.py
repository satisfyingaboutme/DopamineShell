import os,time,platform,socket,re,uuid,json,psutil,logging,subprocess

def gethost():
	return socket.gethostname()

def getcurrentdir():
    cmd = "pwd"
    output = subprocess.check_output(cmd, shell=True, text=True).strip()
    if output in ["/data/data/com.termux/files/home", "/home"]:
        return "~"
    elif output == "/storage/emulated/0":
        return "/sdcard"
    else:
        return output
