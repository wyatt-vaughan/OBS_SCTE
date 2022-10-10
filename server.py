import subprocess
import os
#subprocess.call([r'start.bat'])

commandList = [
    "tsp",
    "--add-input-stuffing 1/10",
    "-I srt 127.0.0.2:9999",
    "-P pmt --service 0001 --add-programinfo-id 0x43554549 --add-pid 600/0x86",
    "-P spliceinject --udp 1000 --service 0001",
    "-P splicemonitor",
    "-P analyze",
    "-P filter --negate --pid 0x1FFF",
    "-O file C:/Users/wvaug/Videos/output.ts"
    
]
def startServer():
    fullCommand = ""
    for command in commandList:
        fullCommand += command+" "
    os.system(fullCommand)
    
startServer()