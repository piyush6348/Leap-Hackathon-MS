import os.path
import pafy
import subprocess
import shutil

def extractAudio(url="", path=""):
    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    bestaudio.download(filepath=path)

def vta(url='https://youtu.be/VJCXwxvLNkY'):
    BASE = "C:\\Users\\Administrator\\Music\\"
    ffmpeg_path = "C:\\ffmpeg-20180712-3ce4034-win64-static\\bin\\ffmpeg"
    source_name = "final.webm"
    source = BASE + source_name
    output_folder = "out"
    if os.path.exists(source):
        os.remove(source)
    if os.path.exists(BASE+output_folder):
        shutil.rmtree(BASE+output_folder)
    os.mkdir(BASE+output_folder)
    destination_name = "sample_output.wav"
    destination = BASE + destination_name
    command = ffmpeg_path + " -y -i " + source + " -ab 160k -ac 2 -ar 44100 -vn " + destination
    ek_aur_command = ffmpeg_path +  " -i " + destination + " -f segment -segment_time 10 -c copy " + BASE + output_folder + "\\out%03d.wav"
    extractAudio(url, source)
    subprocess.call(command,shell=True)
    subprocess.call(ek_aur_command, shell=True)


