import pyshark
import numpy as np
import matplotlib.pyplot as plt

FIRST_SECS=5
STEP=0.05

def plot_graph(filename):
    first_time = 0
    times = range(0, int(FIRST_SECS / STEP) + 1)
    sizes = [0] * len(times)
    count = [0] * len(times)
    with pyshark.FileCapture(f"../{filename}") as capture:
        #,display_filter="(ipv6.dst == 2a06:c701:42ee:b300:98a:9e30:45c2:dcec || ipv6.src == 2a06:c701:42ee:b300:98a:9e30:45c2:dcec || ip.addr == 10.0.0.7)")


        for packet in capture:
            if first_time==0:
                first_time=float(packet.sniff_time.timestamp())

            index=int((float(packet.sniff_time.timestamp())-first_time)/STEP)+1
            if index>=(int(FIRST_SECS/STEP) -1):
                break

            sizes[index]+=(int(packet.length))
            count[index]+=1


    for i in range(len(times)):
        if count[i]>0:
            sizes[i]/=count[i]


    x=np.array(times)*STEP
    y=np.array(sizes)


    plt.plot(x, y,marker='o')
filenames=["chrome.pcapng","edge.pcapng","youtube_Video.pcapng","youtube_Music.pcapng","discord(video conferencing).pcapng"]
for filename in filenames:
    plot_graph(filename)
plt.legend(filenames)
plt.title('Average Packet Size Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Average Packet Size (bytes)')
plt.show()