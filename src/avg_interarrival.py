
import sys
from type import type
import pyshark
import numpy as np
import matplotlib.pyplot as plt

def get_avg_time_interval(filename):
    try:
        with pyshark.FileCapture(f"../pcapng/{filename}",keep_packets=True) as capture:
            list_capture=list(capture)
            length=len(list_capture)
            return (float(list_capture[-1].sniff_time.timestamp())-float(list_capture[0].sniff_time.timestamp()))/(length-1)
    except FileNotFoundError:
        print("Error: file was not found.")
x=0
if type=="bonus":
    x =  ["Bonus(listen to youtube music and send 2 mails).pcapng"]
elif type=="attacker":
    x = ["randomAppUsage.pcapng"]
else:
    x=["chrome.pcapng","edge.pcapng","youtube_Video.pcapng","youtube_Music.pcapng","discord(video conferencing).pcapng"]
#bonus

colors = plt.colormaps['tab10'](np.arange(len(x)))
plt.bar(x, ([get_avg_time_interval(filename) for filename in x]), color=colors)

plt.title('Packets inter-arrival average')
plt.xlabel('')
plt.ylabel('Seconds')
if type=="bonus":
    plt.savefig(f"../res/bonus_{sys.argv[0].split("\\")[-1][:-3]}")
elif type=="attacker":
    plt.savefig(f"../res/randomAppUsage_{sys.argv[0].split("\\")[-1][:-3]}")
else:
    plt.savefig(f"../res/{sys.argv[0].split("\\")[-1][:-3]}")
plt.show()