import pyshark
import numpy as np
import matplotlib.pyplot as plt

FIRST_SECS=5


def plot_graph(filename):
    capture = pyshark.FileCapture(f"../{filename}")
    #,display_filter="(ipv6.dst == 2a06:c701:42ee:b300:98a:9e30:45c2:dcec || ipv6.src == 2a06:c701:42ee:b300:98a:9e30:45c2:dcec || ip.addr == 10.0.0.7)")
    first_time=0
    times = range(0,FIRST_SECS*10+1)
    sizes = [0]*len(times)
    count = [0] * len(times)

    for packet in capture:
        if first_time==0:
            first_time=float(packet.sniff_time.timestamp())

        index=int((float(packet.sniff_time.timestamp())-first_time)/0.1)+1
        if index>=(FIRST_SECS*10 -1):
            break

        sizes[index]+=(int(packet.length))
        count[index]+=1

    capture.close()

    for i in range(len(times)):
        if count[i]>0:
            sizes[i]/=count[i]


    x=np.array(times)/10
    y=np.array(sizes)


    plt.plot(x, y,marker='o')
filenames=["Chrome(google.com).pcapng","Edge(google.com).pcapng","youtube.pcapng","youtubemusic.pcapng","discord(video conferencing).pcapng"]
for filename in filenames:
    plot_graph(filename)
plt.legend(filenames)
plt.title('Average Packet Size Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Average Packet Size (bytes)')
plt.show()