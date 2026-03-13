def build_prompt(query, context, mode="detailed"):

    context_text = ""

    for c in context:
        context_text += c["text"] + "\n\n"

    if mode == "concise":
        instruction = """
Provide a concise answer in 3-4 sentences.
Focus only on the key insight.
"""
    else:
        instruction = """
Provide a detailed explanation with clear structure.
Use bullet points if helpful.
Explain concepts clearly for startup founders.
"""

    prompt = f"""
You are an AI startup research assistant.

Your job is to help users understand startup concepts, funding trends,
business strategy, and market insights.

Use the provided context when available.
If the context contains relevant information, prioritize it.

Context:
{context_text}

Question:
{query}

Instructions:
{instruction}
"""

    return prompt