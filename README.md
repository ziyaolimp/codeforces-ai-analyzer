Markdown

# 🚀 Codeforces AI Performance Analyzer & Coach

An intelligent Django-based web application designed for competitive programmers to analyze their Codeforces submissions, identify algorithmic weaknesses, and receive personalized AI-driven roadmaps and interactive coaching.

---

## 🌟 Features

- **Codeforces API Integration:** Automatically fetches and processes a user's submission history and problem tags.
- **Dual-Metric Analysis:** Evaluates correct vs. incorrect submission patterns to accurately pinpoint weak algorithmic topics (e.g., Dynamic Programming, Graphs, Bit Manipulation).
- **AI-Powered Roadmaps:** Leverages the Groq API to generate tailored, step-by-step study and practice roadmaps.
- **Interactive AI Coach:** Session-based contextual chat interface allowing users to ask follow-up questions, discuss problem-solving strategies, and get real-time guidance.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
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

2. Create and activate a virtual environment
Bash

python -m venv venv
# On Windows:
venv\Scripts\Activate
# On macOS/Linux:
source venv/bin/activate

3. Install dependencies
Bash

pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the root directory and add your Groq API key:
Kod hissəsi

GROQ_API_KEY=your_actual_groq_api_key_here

5. Apply database migrations
Bash

python manage.py migrate

6. Run the development server
Bash

python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/.
💡 Usage

    Enter your Codeforces handle on the home page.

    View your performance analytics and identified weak tags.

    Generate an AI-powered roadmap to target your weak spots.

    Use the interactive coach chat to dive deeper into specific problem-solving techniques.

👤 Author

Ziya Hasanov

    GitHub: @ziyaolimp