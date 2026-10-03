# AI Emotion-Aware Task Optimizer

An intelligent task optimization system that dynamically schedules daily academic, work, and personal tasks based on real-time emotional state detection. By pairing OpenCV facial recognition with foundational Artificial Intelligence search and optimization algorithms, the system minimizes mental burn-out and aligns user energy levels with task complexity.

---

## Key Features

* **Real-Time Emotion Recognition:** Uses `FER` (Facial Emotion Recognition with MTCNN) via OpenCV to capture and classify live facial expressions.
* **Algorithmic Task Optimization:** Incorporates five distinct decision-making algorithms to evaluate and select the best tasks based on emotion-task fit and priority.
* **Automated Distress Interventions:** Detects negative affective states (e.g., distress, anger, sadness, fatigue) and automatically triggers forced break cycles.
* **Customizable User Preferences:** Supports customized task lists for both **Students** and **Employees**, spanning academic/work, personal life, and break activities.

---

## System Architecture & Team Contributions

The system processes real-time camera frames, evaluates current emotional state against the user's task bank via **Constraint Satisfaction Filtering (CSP)**, and then passes candidates to heuristic search algorithms:

| Contributor | Algorithm Implementation | Role in Optimization Pipeline |
| :--- | :--- | :--- |
| **Judy** | **CSP Filter** (`csp_filter`) | Filters tasks to ensure hard constraint matching between detected emotion and `emotion_fit`. |
| **Marwan** | **Greedy Search** (`greedy`) | Selects the candidate task with the absolute highest priority score. |
| **Idrees** | **Hill Climbing** (`hill_climbing`) | Finds locally optimal task transitions close in priority to the current active task. |
| **Mariam** | **Stochastic Selection** (`stochastic`) | Performs weighted random task selection proportional to priority levels. |
| **Farida** | **Mini A* Search** (`mini_a_star`) | Evaluates tasks using a combined heuristic score based on priority and emotional compatibility. |

---

## Directory Structure

```text
.
├── algorithms.py              # Algorithmic decision engine (CSP, Greedy, Hill Climbing, Stochastic, Mini A*)
├── check_libraries.py         # Diagnostic utility script for verifying dependencies
├── emotion_detector.py        # OpenCV & FER camera stream integration
├── emotion_task_optimizer.py # Main application orchestration loop (Task Mode)
├── preferences.py            # Advanced profile and task input collector
└── tasks.py                   # Task data structure definition and interactive user input prompts

Installation & Setup
1. Prerequisites
Ensure you have Python 3.8+ installed along with a working webcam device.

2. Clone Repository

git clone [https://github.com/Yousuf-Idrees/AI_Emotion_Task_Optimizer.git](https://github.com/Yousuf-Idrees/AI_Emotion_Task_Optimizer.git)
cd AI_Emotion_Task_Optimizer

3. Install Dependencies
Install the required computer vision and deep learning packages:

pip install fer opencv-python torch torchvision numpy

4. Verify Dependencies
Run the diagnostic script to ensure all libraries are installed correctly:

python check_libraries.py

Usage
Launch the main application:

python emotion_task_optimizer.py

Setup User Profile: Select your profile (Student/Employee) and input your tasks, priorities (1–5), and break activities when prompted.
Activate Task Mode: Enter y when asked to start Task Mode.
Live Execution: The webcam stream will initialize, evaluate your current emotional state in 30-second cycles, run the algorithmic suite, and output optimal task recommendations in your terminal.
Exit: Press q in the terminal or camera window to safely terminate execution.
