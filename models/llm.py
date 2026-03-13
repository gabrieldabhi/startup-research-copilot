from groq import Groq
from config.config import GROQ_API_KEY, LLM_MODEL


client = Groq(api_key=GROQ_API_KEY)


def generate_response(prompt):

    try:

        completion = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        print("LLM error:", e)
        return "Sorry, the AI could not generate a response due to an internal error."