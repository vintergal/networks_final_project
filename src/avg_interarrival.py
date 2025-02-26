import pyshark
import numpy as np
import matplotlib.pyplot as plt

def get_avg_time_interval(filename):
    with pyshark.FileCapture(f"../{filename}",keep_packets=True) as capture:
        list_capture=list(capture)
        length=len(list_capture)
        return (float(list_capture[-1].sniff_time.timestamp())-float(list_capture[0].sniff_time.timestamp()))/(length-1)

x=filenames=["chrome.pcapng","edge.pcapng","youtube_Video.pcapng","youtube_Music.pcapng","discord(video conferencing).pcapng"]
colors = plt.colormaps['tab10'](np.arange(len(filenames)))
plt.bar(x, ([get_avg_time_interval(filename) for filename in filenames]), color=colors)

plt.title('Packets inter-arrival average')
plt.xlabel('')
plt.ylabel('Seconds')
plt.show()