# AI-Powered Reddit Persona Generator


An advanced command-line tool that leverages the power of Google's Gemini AI to create detailed, structured user personas from a Reddit user's public comment and submission history.

---

## Overview

This project provides a seamless workflow to analyze a Reddit user's online behavior and generate a comprehensive persona. It automates the process of data collection via the Reddit API and performs sophisticated analysis using a specifically engineered prompt for the Gemini LLM. The final output is a detailed text file outlining the user's inferred demographics, personality traits, motivations, goals, and frustrations, with every point justified by a direct quote from the user's history.

This tool is perfect for user research, market analysis, or anyone interested in applying LLMs to understand digital behavior.

## Features

-   **AI-Powered Analysis:** Utilizes Google's `gemini-1.5-flash` model for nuanced and detailed persona generation.
-   **Direct Reddit Integration:** Uses the official Reddit API via `PRAW` to fetch the latest user comments and posts.
-   **Evidence-Based Output:** Every inferred trait in the final persona is backed by a direct quote from the user's data, ensuring transparency and accuracy.
-   **Structured & Detailed Personas:** Generates a multi-section report including demographics, a Myers-Briggs style analysis, motivations, habits, goals, and frustrations.
-   **Secure Credential Management:** Uses a `.env` file to keep your API keys safe and out of the source code.
-   **Easy to Use:** Simply provide a Reddit user's profile URL to get a complete analysis.

## How It Works

1.  **Input:** The user runs `main.py` from the command line, providing a URL to a Reddit user's profile (e.g., `https://www.reddit.com/user/someuser`).
2.  **Scraping:** The `scraper.py` module connects to the Reddit API using your credentials and fetches the user's most recent comments and post submissions.
3.  **AI Analysis:** The collected data is passed to the `llm.py` module. It constructs a highly detailed prompt and sends the user's data to the Gemini API.
4.  **Generation:** The Gemini model analyzes the data according to the prompt's strict instructions and generates the persona text.
5.  **Output:** The script saves the generated persona into a text file named `{username}_persona.txt` in the project directory.

## Getting Started

### Prerequisites

-   Python 3.7+
-   A Reddit account and API credentials.
-   A Google AI Studio account and a Gemini API key.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/frickyouu/redditpersonagenerator.git](https://github.com/frickyouu/redditpersonagenerator.git)
    cd redditpersonagenerator
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file with the following content:)*
    ```
    praw
    google-generativeai
    python-dotenv
    ```

### Configuration

1.  Create a file named `.env` in the root of the project directory.
2.  Add your API credentials to the `.env` file like this:

    ```env
    # Reddit API Credentials
    REDDIT_CLIENT_ID="YOUR_REDDIT_CLIENT_ID"
    REDDIT_CLIENT_SECRET="YOUR_REDDIT_CLIENT_SECRET"
    REDDIT_USER_AGENT="PersonaGenerator/1.0 by YourUsername"

    # Google Gemini API Key
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```

## Usage

Run the main script from your terminal, followed by the full URL of the Reddit user's profile you want to analyze.

```bash
python main.py "[https://www.reddit.com/user/spez](https://www.reddit.com/user/spez)"
```

After the script finishes, you will find a `spez_persona.txt` file in your project folder.

## Troubleshooting

If you encounter connection issues, use the provided test scripts to diagnose the problem:

-   **Test Reddit Connection:**
    ```bash
    python test.py
    ```
-   **Test Gemini Connection:**
    ```bash
    python test_gemini.py
    ```
These scripts will help confirm if your credentials in the `.env` file are correct.

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, please fork the repository and submit a pull request.

python test_gemini.py

These scripts will help confirm if your credentials in the .env file are correct.

Contributing
Contributions are welcome! If you have ideas for new features or improvements, please fork the repository and submit a pull request.
