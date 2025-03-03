# Communication Networks – Encrypted Network Traffic Analysis and Classification

## Project Overview
This project analyzes traffic characteristics of common apps (web browsing, streaming, video conferencing) and explores how attackers can infer user activity from encrypted traffic. Key tasks include:
- Capturing network traffic using Wireshark
- Analyzing packet sizes, flow volume, and inter-arrival times
- Simulating attack scenarios and proposing mitigation techniques

---

## How to Run
### Requirements:
- Linux environment / Windows environment
- Python 3 (clean installation)
- Install dependencies:
```bash
pip install numpy matplotlib pyshark
```
- You must have pcap files to run the code on. Please add your own pcap files to the `/pcapng/` directory!

### Run the Analysis:
```bash
git clone https://github.com/vintergal/networks_final_project
cd networks_final_project
cd src
python avg_packet_size.py
python packets_count.py
python flow_volume.py
python avg_interarrival.py

```
- if install not working, use the next commands:
in the networks_final_project
```bash

python3 -m venv myenv
source myenv/bin/activate
pip install numpy
pip install matplotlib
pip install pyshark 
```

Results are shown in the `/res/` folder.

---

## Project Structure
```
/project-root
│
├── README.md                 # Project instructions
├── final_report.pdf          # Full report with paper summaries
├── /src/                     # Python code
├── /res/                     # Analysis results (figures, plots)
├── /papers/                  # Research papers (excluded from GitHub)
└── /pcapng/                    # pcapng files from wireshark (excluded from GitHub)

```

---


## Contributors
- Adi Moskovich
- Gal Vinter
- Roei Yanku
- Ori Shpitz
---

## Submission Details
- GitHub repo includes the full code, results, and final report.
- `.pcapng` files provided via cloud links (not included in GitHub).
- Code handles edge cases, uses relative paths, and is Linux-compatible.

