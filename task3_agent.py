from datetime import datetime
import math
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Multi-Tool Autonomous Agent", page_icon="🤖")

st.title("🤖 Task 3: Multi-Tool Autonomous AI Agent")
st.markdown(
    "Yeh agent user ki query ko analyze kar ke khud decide karta hai ke konsa"
    " **Tool** execute karna hai."
)

# Available Tools Sidebar
st.sidebar.header("🛠️ Agent's Available Tools")
st.sidebar.success("1. 🧮 Calculator Tool (Math evaluation)")
st.sidebar.info("2. 📅 Date & Time Tool (System clock)")
st.sidebar.warning("3. 📚 Knowledge Base Tool (AI & LangChain info)")


# --- TOOL DEFINITIONS ---
def calculator_tool(expression):
  try:
    # Safe evaluation for basic math
    allowed_names = {"sqrt": math.sqrt, "pow": pow}
    result = eval(expression, {"__builtins__": None}, allowed_names)
    return f"Calculated Result: {result}"
  except Exception:
    return "Error: Invalid mathematical expression."


def datetime_tool():
  now = datetime.now()
  return f"Current Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S (%A)')}"


def knowledge_tool(query):
  kb = {
      "rag": (
          "RAG (Retrieval-Augmented Generation) connects LLMs to external"
          " documents for accurate, grounded answers."
      ),
      "langchain": (
          "LangChain is an open-source framework for building LLM-powered"
          " applications, chains, and autonomous agents."
      ),
      "agent": (
          "An AI Agent uses an LLM as a reasoning engine to choose which tools"
          " to call and in what order."
      ),
  }
  for key, val in kb.items():
    if key in query.lower():
      return val
  return (
      "Topic not found in local Knowledge Base, answering via general LLM"
      " reasoning."
  )


# --- AUTONOMOUS AGENT ROUTER (REASONING ENGINE) ---
def run_autonomous_agent(user_query):
  query_lower = user_query.lower()
  thought_process = []

  # Step 1: Analyze Intent & Select Tool
  if any(
      op in query_lower
      for op in ["+", "-", "*", "/", "calculate", "math", "sqrt"]
  ):
    thought_process.append(
        "🤔 **Thought:** User is asking a math question. I should invoke the"
        " **Calculator Tool**."
    )
    # Extract math part simply
    clean_expr = "".join(
        c for c in user_query if c in "0123456789+-*/(). sqrtpow"
    ).strip()
    thought_process.append(
        f"⚙️ **Action:** Calling `calculator_tool('{clean_expr}')`"
    )
    observation = calculator_tool(clean_expr)

  elif any(word in query_lower for word in ["time", "date", "day", "today"]):
    thought_process.append(
        "🤔 **Thought:** User wants temporal information. I should invoke the"
        " **Date & Time Tool**."
    )
    thought_process.append("⚙️ **Action:** Calling `datetime_tool()`")
    observation = datetime_tool()

  elif any(
      word in query_lower
      for word in ["rag", "langchain", "agent", "what is"]
  ):
    thought_process.append(
        "🤔 **Thought:** User is asking a technical AI question. I should"
        " search the **Knowledge Base Tool**."
    )
    thought_process.append(
        f"⚙️ **Action:** Calling `knowledge_tool('{user_query}')`"
    )
    observation = knowledge_tool(user_query)

  else:
    thought_process.append(
        "🤔 **Thought:** No external tool required. Answering directly using"
        " base LLM knowledge."
    )
    observation = (
        "Direct Response: Hello! I am your Autonomous AI Assistant. Ask me"
        " to calculate math, check the date/time, or explain RAG/LangChain!"
    )

  thought_process.append(f"👁️ **Observation:** {observation}")
  return thought_process, observation


# --- STREAMLIT UI ---
st.subheader("💬 Give the Agent a Task")
sample_prompts = [
    "Calculate 25 * 48 + 100",
    "What is today's date and time?",
    "What is RAG in AI?",
    "Hello, who are you?",
]
selected_sample = st.selectbox(
    "Try a sample prompt (or type your own below):", ["Custom"] + sample_prompts
)

if selected_sample != "Custom":
  user_input = st.text_input("Your Prompt:", value=selected_sample)
else:
  user_input = st.text_input(
      "Your Prompt:", placeholder="e.g., Calculate 144 / 12 or What is an agent?"
  )

if st.button("🚀 Run Agent"):
  if user_input.strip():
    with st.spinner("Agent is reasoning and selecting tools..."):
      thoughts, final_answer = run_autonomous_agent(user_input)

      st.markdown("### 🧠 Agent Reasoning Trace (ReAct Pattern)")
      for step in thoughts:
        st.write(step)

      st.success(f"**✅ Final Answer:** {final_answer}")
  else:
    st.warning("Please enter a prompt first!")