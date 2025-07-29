# 🧠 Operating System Lab – CPU Scheduling Algorithms in Python

Welcome to the **CPU Scheduling Algorithms** collection implemented in **Python** 🐍.  
This repository demonstrates the core CPU scheduling techniques commonly taught in Operating Systems (OS) labs.

📌 Suitable for students, educators, and OS enthusiasts who want to understand scheduling behavior through Python code.

---

## 📚 Implemented Algorithms

### 🔹 1. First-Come, First-Serve (FCFS)

- **Type**: Non-preemptive  
- **Description**:  
  Processes are executed in the order they arrive. Each job runs to completion before the next one starts.

- **Highlights**:
  - Simple to implement
  - Can cause long waiting time for short processes (Convoy effect)
  - Fair, based on arrival order

**Example Usage**:
```python
processes = [
    {"pid": "P3", "arrival": 0, "burst": 2},
    {"pid": "P1", "arrival": 3, "burst": 1},
    {"pid": "P4", "arrival": 3, "burst": 7},
    {"pid": "P2", "arrival": 4, "burst": 5},
    {"pid": "P5", "arrival": 5, "burst": 5},
]

fcfs(processes)
```

## Report
You can find the detailed project report here: [FCFS](https://drive.google.com/file/d/1joVQVtMjTn1fvozP9Svcc-Qt2iqOej-R/view?usp=drive_link)
