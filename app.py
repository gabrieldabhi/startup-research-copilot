import streamlit as st

from utils.router import route_query, explain_route
from utils.rag_pipeline import build_vector_store, retrieve_context
from utils.web_search import search_web
from utils.prompt_builder import build_prompt
from models.llm import generate_response


DATA_PATH = "data/startup_docs"


st.set_page_config(
    page_title="Startup Research Copilot",
    layout="wide"
)

st.title("Startup Research Copilot")

st.markdown(
"""
AI assistant for **startup strategy, funding insights, and market research**  
Powered by **RAG + Web Search + LLM reasoning**
"""
)

st.divider()


# Sidebar settings
st.sidebar.header("Settings")

mode_option = st.sidebar.selectbox(
    "Response Style",
    ["Detailed Analysis", "Concise Summary"]
)

if mode_option == "Detailed Analysis":
    mode = "detailed"
else:
    mode = "concise"

st.sidebar.markdown(
"""
**Detailed Analysis**
- Longer explanations
- Structured responses

**Concise Summary**
- Short answers
- Quick insights
"""
)


st.sidebar.divider()

st.sidebar.markdown("### About")

st.sidebar.info(
"""
Startup Research Copilot helps users explore:

• Startup strategy  
• Venture capital funding  
• Market trends  
• Competitor insights  

Powered by **RAG + Web Search + LLM reasoning**
"""
)

st.sidebar.markdown("### Example Questions")

st.sidebar.write(
"""
• What is product market fit?  
• Latest AI startup funding trends  
• Why do startups fail?
"""
)


# Cache vector database
@st.cache_resource
def load_vector_store():
    try:
        return build_vector_store(DATA_PATH)
    except Exception as e:
        st.error(f"Vector database failed to load: {e}")
        return None, None, None


index, chunks, metadata = load_vector_store()


# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def run_query(query):

    try:
        route = route_query(query)

        context = []

        if route == "rag":

            try:
                results = retrieve_context(query, index, chunks, metadata)

                for r in results:
                    context.append({
                        "text": r["text"],
                        "source": r["source"]
                    })

            except Exception as e:
                st.error(f"RAG retrieval failed: {e}")

        elif route == "web":

            try:
                results = search_web(query)

                for r in results:
                    context.append({
                        "text": r["content"],
                        "source": r["url"]
                    })

            except Exception as e:
                st.error(f"Web search failed: {e}")

        prompt = build_prompt(query, context, mode)

        response = generate_response(prompt)

        return response, context, route

    except Exception as e:
        st.error(f"System error: {e}")
        return "An unexpected error occurred.", [], "error"


query = st.chat_input("Ask a startup question...")


if query:

    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.chat_message("user"):
        st.write(query)

    with st.spinner("Analyzing knowledge sources..."):

        answer, sources, route = run_query(query)

    with st.chat_message("assistant"):

        st.write(answer)

        st.write("### Sources")

        unique_sources = set()

        for s in sources:
            unique_sources.add(s["source"])

        for src in unique_sources:
            st.write("-", src)

        st.write("### Reasoning")
        st.write(explain_route(route))

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })