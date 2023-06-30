import pyperclip
import ffmpeg
strin = '''console.log(jwplayer("rvcMediaPlayer").getConfig()["playlist"][0]["sources"][0]["file"])'''

print(strin)

copy_to_clipboard = input("Do you want to copy the command to clipboard? (y/n): ")

if copy_to_clipboard.lower() == "y":
    pyperclip.copy(strin)
    print("Command copied to clipboard.")
else:
    print("Command not copied.")

while True:
    try:
        linkin = input()
        fname = linkin.split('''/playlist.m3u8''')[0].split('''mp4:''')[1].replace(".mp4",".ts")
        (
            ffmpeg
            .input(linkin)
            .output(fname,acodec='copy',vcodec='copy')
            .run()
        )
    except KeyboardInterrupt:
        # User pressed Ctrl+C
        print("Program interrupted by user")
        break
    except Exception as e:
        print(e)
        continue
    else: #no error
        break