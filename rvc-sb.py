import pyperclip
import ffmpeg
strin = '''console.log(jwplayer("rvcplayer").getConfig()["playlist"][0]["sources"][0]["file"])'''

#pyperclip.copy(strin)

linkin = input()
fname = linkin.split('''/playlist.m3u8''')[0].split('''mp4:''')[1].replace(".mp4",".ts")
(
    ffmpeg
    .input(linkin)
    .output(fname,acodec='copy',vcodec='copy')
    .run()
)