import pyshark
import numpy as np
import matplotlib.pyplot as plt

FIRST_SECS=5
STEP=0.05

def plot_graph(filename):
    first_time = 0
    times = range(0, int(FIRST_SECS / STEP) + 1)
    sizes = [0] * len(times)
    with pyshark.FileCapture(f"../{filename}") as capture:
        #,display_filter="(ipv6.dst == 2a06:c701:42ee:b300:98a:9e30:45c2:dcec || ipv6.src == 2a06:c701:42ee:b300:98a:9e30:45c2:dcec || ip.addr == 10.0.0.7)")


        for packet in capture:
            if first_time==0:
                first_time=float(packet.sniff_time.timestamp())

            index=int((float(packet.sniff_time.timestamp())-first_time)/STEP)+1
            if index>=(int(FIRST_SECS/STEP) -1):
                break

            sizes[index]+=(int(packet.length))

        x = np.array(times) * STEP
        length = len(x)
        sizes = np.array(sizes)
        matrix = (1 - np.tril(np.ones([length, length]), -1))
        y = sizes.dot(matrix)/1e3

    plt.plot(x, y,marker='o')
filenames=["chrome.pcapng","edge.pcapng","youtube_Video.pcapng","youtube_Music.pcapng","discord(video conferencing).pcapng"]
for filename in filenames:
    plot_graph(filename)
plt.legend(filenames)
plt.title('Flow volume - overall number of kilobytes transmitted')
plt.xlabel('Time (seconds)')
plt.ylabel('Size (Kilobytes)')
plt.show()



