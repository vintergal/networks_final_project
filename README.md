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
pip install pandas numpy matplotlib pyshark
```

### Run the Analysis:
```bash
git clone <repository_link>
cd <repository_name>/src
python analyze_traffic.py
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
└── /pcap/                    # pcap files from wireshark (excluded from GitHub)

```

---


## Contributors
- Gal Vinter
- Roei Yanku
- Adi Moskovich
- Ori Shpitz
---

## Submission Details
- GitHub repo includes the full code, results, and final report.
- `.pcap` files provided via cloud links (not included in GitHub).
- Code handles edge cases, uses relative paths, and is Linux-compatible.

