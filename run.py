import subprocess

command = 'python yolov5/detect.py --weights best.pt --img 416 --conf 0.5 --source 0'
subprocess.run(command, shell=True)
