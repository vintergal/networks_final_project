
import sys
from is_bonus import is_bonus
import pyshark
import numpy as np
import matplotlib.pyplot as plt

FIRST_SECS = 0
if is_bonus:
    FIRST_SECS=30
else:
    FIRST_SECS=5
STEP=0.05

def plot_graph(filename):
    first_time = 0
    times = range(0, int(FIRST_SECS / STEP) + 1)
    count = [0] * len(times)
    with pyshark.FileCapture(f"../{filename}") as capture:
        #,display_filter="(ipv6.dst == 2a06:c701:42ee:b300:98a:9e30:45c2:dcec || ipv6.src == 2a06:c701:42ee:b300:98a:9e30:45c2:dcec || ip.addr == 10.0.0.7)")


        for packet in capture:
            if first_time==0:
                first_time=float(packet.sniff_time.timestamp())

            index=int((float(packet.sniff_time.timestamp())-first_time)/STEP)+1
            if index>=(int(FIRST_SECS/STEP) -1):
                break

            count[index]+=1


    x=np.array(times)*STEP
    length=len(x)
    count=np.array(count)
    matrix=(1-np.tril(np.ones([length,length]),-1))
    y=count.dot(matrix)

    plt.plot(x, y,marker='o')
x=0
if is_bonus:
    x = filenames = ["Bonus(listen to youtube music and send 2 mails).pcapng"]
else:
    x=filenames=["chrome.pcapng","edge.pcapng","youtube_Video.pcapng","youtube_Music.pcapng","discord(video conferencing).pcapng"]
for filename in filenames:
    plot_graph(filename)
plt.legend(filenames)
plt.title('Packets count Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Number of packets')
if is_bonus:
    plt.savefig(f"../res/bonus_{sys.argv[0].split("\\")[-1][:-3]}")
else:
    plt.savefig(f"../res/{sys.argv[0].split("\\")[-1][:-3]}")
plt.show()