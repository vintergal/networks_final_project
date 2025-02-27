
import sys
from is_bonus import is_bonus
import pyshark
import numpy as np
import matplotlib.pyplot as plt

def get_avg_time_interval(filename):
    with pyshark.FileCapture(f"../{filename}",keep_packets=True) as capture:
        list_capture=list(capture)
        length=len(list_capture)
        return (float(list_capture[-1].sniff_time.timestamp())-float(list_capture[0].sniff_time.timestamp()))/(length-1)
x=0
if is_bonus:
    x = filenames = ["Bonus(listen to youtube music and send 2 mails).pcapng"]
else:
    x=filenames=["chrome.pcapng","edge.pcapng","youtube_Video.pcapng","youtube_Music.pcapng","discord(video conferencing).pcapng"]
#bonus

colors = plt.colormaps['tab10'](np.arange(len(filenames)))
plt.bar(x, ([get_avg_time_interval(filename) for filename in filenames]), color=colors)

plt.title('Packets inter-arrival average')
plt.xlabel('')
plt.ylabel('Seconds')
if is_bonus:
    plt.savefig(f"../res/bonus_{sys.argv[0].split("\\")[-1][:-3]}")
else:
    plt.savefig(f"../res/{sys.argv[0].split("\\")[-1][:-3]}")
plt.show()