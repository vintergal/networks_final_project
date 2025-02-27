
import sys
from type import type
import pyshark
import numpy as np
import matplotlib.pyplot as plt

FIRST_SECS = 0
if type=="bonus" or type=="attacker":
    FIRST_SECS=30
else:
    FIRST_SECS=5
STEP=0.05

def plot_graph(filename):
    first_time = 0
    times = range(0, int(FIRST_SECS / STEP) + 1)
    count = [0] * len(times)
    try:
        with pyshark.FileCapture(f"../pcapng/{filename}") as capture:
            for packet in capture:
                if first_time==0:
                    first_time=float(packet.sniff_time.timestamp())

                index=int((float(packet.sniff_time.timestamp())-first_time)/STEP)+1
                if index>=(int(FIRST_SECS/STEP) -1):
                    break

                count[index]+=1
    except FileNotFoundError:
        print("Error: file was not found or file is empty/corrupt.")


    x=np.array(times)*STEP
    length=len(x)
    count=np.array(count)
    matrix=(1-np.tril(np.ones([length,length]),-1))
    y=count.dot(matrix)

    plt.plot(x, y,marker='o')
x=0
if type=="bonus":
    x =  ["Bonus(listen to youtube music and send 2 mails).pcapng"]
elif type=="attacker":
    x = ["randomAppUsage.pcapng"]
else:
    x=["chrome.pcapng","edge.pcapng","youtube_Video.pcapng","youtube_Music.pcapng","discord(video conferencing).pcapng"]
for filename in x:
    plot_graph(filename)
plt.legend(x)
plt.title('Packets count Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Number of packets')
if type=="bonus":
    plt.savefig(f"../res/bonus_{sys.argv[0].split("\\")[-1][:-3]}")
elif type=="attacker":
    plt.savefig(f"../res/randomAppUsage_{sys.argv[0].split("\\")[-1][:-3]}")
else:
    plt.savefig(f"../res/{sys.argv[0].split("\\")[-1][:-3]}")
#plt.show()
print("The image has been added to the /res/ directory")