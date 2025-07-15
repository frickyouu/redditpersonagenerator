import os
import google.generativeai as genai
from dotenv import load_dotenv

def generate_persona(user_data: list, username: str):

    model = genai.GenerativeModel('gemini-1.5-flash')
    
    combined_data = "\n\n".join(user_data)
    
    prompt = f"""
    You are an expert AI analyst. Your task is to create a detailed user persona based on the following collection of a Reddit user's posts and comments.

    The final output must strictly follow the structure and sections outlined below.

    **CRITICAL INSTRUCTION:** For every single piece of information, trait, goal, or frustration you list, you **MUST** provide a direct quote from the user's posts or comments as a "Source" to justify your analysis.

    ---
    **Persona Structure to Follow:**

    **[User's Name/Username]**

    > "Generate a representative, one-sentence quote that encapsulates the user's core motivation or frustration."
    > **Source:** "[Quote the full user comment that inspired this.]"

    ## Demographics
    - **Age:** [Infer age] - **Source:** "[Quote source text]"
    - **Occupation:** [Infer occupation] - **Source:** "[Quote source text]"
    - **Location:** [Infer location] - **Source:** "[Quote source text]"
    - **Status:** [Infer relationship status, e.g., Single, Married] - **Source:** "[Quote source text]"
    - **Archetype:** [Assign a creative archetype, e.g., The Creator, The Explorer] - **Source:** "[Quote source text that supports this archetype]"

    ## Personality & Traits (Myers-Briggs Style Analysis)
    - **Introvert vs. Extrovert:** [Analyze and state where they likely fall] - **Source:** "[Quote source text]"
    - **Sensing vs. Intuition:** [Analyze and state where they likely fall] - **Source:** "[Quote source text]"
    - **Thinking vs. Feeling:** [Analyze and state where they likely fall] - **Source:** "[Quote source text]"
    - **Judging vs. Perceiving:** [Analyze and state where they likely fall] - **Source:** "[Quote source text]"

    ## Motivations
    *A list of key drivers for the user's behavior.*
    - [Inferred motivation, e.g., Seeking Convenience] - **Source:** "[Quote source text]"
    - [Inferred motivation, e.g., Desire for Wellness] - **Source:** "[Quote source text]"
    - [Inferred motivation, e.g., Valuing Speed/Efficiency] - **Source:** "[Quote source text]"

    ## Behaviour & Habits
    *A list of typical behaviors observed from the data.*
    - [Observed habit, e.g., Orders takeaways frequently] - **Source:** "[Quote source text]"
    - [Observed habit, e.g., Engages in online tech discussions] - **Source:** "[Quote source text]"
    - [Observed habit, e.g., Prefers healthy food options] - **Source:** "[Quote source text]"

    ## Goals & Needs
    *A list of what the user is trying to achieve.*
    - [Identified goal, e.g., Wants to enjoy a healthy diet] - **Source:** "[Quote source text]"
    - [Identified need, e.g., Needs detailed information before deciding] - **Source:** "[Quote source text]"
    - [Identified goal, e.g., Wants to balance work and healthy lifestyle] - **Source:** "[Quote source text]"

    ## Frustrations
    *A list of pain points, challenges, or things they dislike.*
    - [Identified frustration, e.g., Wasting time on confusing menus] - **Source:** "[Quote source text]"
    - [Identified frustration, e.g., Lack of healthy options] - **Source:** "[Quote source text]"
    - [Identified frustration, e.g., Unclear pre-order options] - **Source:** "[Quote source text]"
    ---

    **Reddit User Data:**

    {combined_data}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while generating the persona: {e}"
