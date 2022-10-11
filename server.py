import subprocess
import os


commandList = [
    # tsp is the command for most TSduck commands
    "tsp",
    
    # adds stuffing to the stream so the SCTE can be injected
    "--add-input-stuffing 1/10",
    
    # is the input over srt that also needs to be what OBS streams to
    "-I srt 127.0.0.2:9999",
    
    # adds the new service that follows SCTE-35 guidelines
    "-P pmt --service 0001 --add-programinfo-id 0x43554549 --add-pid 600/0x86",
    
    # listens over udp port 1000 for a XML to splice into the stream
    "-P spliceinject --udp 1000 --service 0001",
    
    # a monitor to see when SCTE is injected
    "-P splicemonitor",
    
    # outputs a report after stream ends
    "-P analyze",
    
    # removes extra stuffing at the end
    "-P filter --negate --pid 0x1FFF",
    
    # specifies where the output file should be stored
    "-O file video_output.ts"
    
]
def startServer():
    fullCommand = ""
    for command in commandList:
        fullCommand += command+" "
    os.system(fullCommand)
    
startServer()
