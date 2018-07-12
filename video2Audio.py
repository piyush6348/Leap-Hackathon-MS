import os.path
import pafy
import subprocess
import shutil

def extractAudio(url="", path=""):
    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    bestaudio.download(filepath=path)

def vta(url='https://youtu.be/VJCXwxvLNkY'):
    BASE = os.getcwd()
    BASE_OUT = os.path.join(BASE, "out")
    ffmpeg_path = "C:\\ffmpeg-20180712-3ce4034-win64-static\\bin\\ffmpeg"
    source_name = "final.webm"
    source = os.path.join(BASE, source_name)
    output_folder = "out"
    if os.path.exists(source):
        os.remove(source)
    if os.path.exists(BASE_OUT):
        shutil.rmtree(BASE_OUT)
    os.mkdir(BASE_OUT)
    destination_name = "sample_output.wav"
    destination = os.path.join(BASE, destination_name)
    command = ffmpeg_path + " -y -i " + source + " -ab 160k -ac 2 -ar 44100 -vn " + destination
    ek_aur_command = ffmpeg_path +  " -i " + destination + " -f segment -segment_time 10 -c copy " + os.path.join(BASE_OUT,"out%03d.wav")
    extractAudio(url, source)
    # print (command, ek_aur_command)
    subprocess.call(command,shell=True)
    subprocess.call(ek_aur_command, shell=True)

vta()
