# 🚀 Codeforces AI Performance Analyzer & Coach

An intelligent Django-based web application designed for competitive programmers to analyze their Codeforces submissions, identify algorithmic weaknesses, and receive personalized AI-driven roadmaps and interactive coaching.

---

## 🌟 Features

- **Codeforces API Integration:** Automatically fetches and processes a user's submission history and problem tags.
- **Dual-Metric Analysis:** Evaluates correct vs. incorrect submission patterns to accurately pinpoint weak algorithmic topics (e.g., Dynamic Programming, Graphs, Bit Manipulation).
- **AI-Powered Roadmaps:** Leverages the Groq API (`gpt-oss-120b`) to generate tailored, step-by-step study and practice roadmaps.
- **Interactive AI Coach:** Session-based contextual chat interface allowing users to ask follow-up questions, discuss problem-solving strategies, and get real-time guidance.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django 6.1.2
- **APIs:** Codeforces API, Groq API
- **Database:** SQLite (Development)
- **Frontend:** HTML5, CSS3, JavaScript

---

## ⚙️ Installation & Setup

To run this project locally on your machine, follow these steps:

### 1. Clone the repository
```bash
git clone [https://github.com/ziyaolimp/codeforces-ai-analyzer.git](https://github.com/ziyaolimp/codeforces-ai-analyzer.git)
cd codeforces-ai-analyzer