import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.calculator import calculate
from tools.file_reader import read_file
from tools.web_search import web_search


load_dotenv()


@tool
def calculator_tool(expression: str) -> str:
    """Evaluate a mathematical expression. Input should be a math expression."""
    return str(calculate(expression))


@tool
def file_reader_tool(filename: str) -> str:
    """Read a supported text file from the local data directory. Input is its filename."""
    return read_file(filename)


@tool
def web_search_tool(query: str) -> str:
    """Search the web for current information. Input should be a search query."""
    return web_search(query)


def build_agent():
    if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add it to your .env file."
        )

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
    )

    tools = [
        calculator_tool,
        file_reader_tool,
        web_search_tool,
    ]

    return create_agent(
        model=model,
        tools=tools,
        system_prompt=(
            "You are NexusAI, a helpful multi-tool AI agent. "
            "Use the calculator for mathematical calculations","the web search "
            "tool for current information, and the file reader for questions "
            "about local files. You may use multiple tools when necessary. "
            "Base your answers on tool results and clearly state when information "
            "could not be verified. Never claim a tool succeeded if it failed."
            "First find the answer for the query from the RAG DataBase , if the answer is not found"
            " then use the web search tool to find the answer. If the answer is still not found, use the calculator tool to calculate the answer. If the answer is still not found, use the file reader tool to read the answer from a local file."
        ),
    )



def ask_agent(agent, question: str) -> str:
    """Run the agent, display tool execution logs, and return its final answer."""
    response = agent.invoke(
        {"messages": [{"role": "user", "content": question}]}
    )

    for message in response["messages"]:
        tool_calls = getattr(message, "tool_calls", None) or []

        for call in tool_calls:
            print(f"\n[Tool Action] {call['name']}")
            print(f"[Input] {call['args']}")

        if getattr(message, "type", "") == "tool":
            content = message.content

            if isinstance(content, list):
                content = "\n".join(
                    block.get("text", str(block))
                    if isinstance(block, dict)
                    else str(block)
                    for block in content
                )

            observation = str(content)
            if len(observation) > 1000:
                observation = observation[:1000] + "... [truncated]"

            print(f"[Observation: {message.name}]")
            print(observation)

    for message in reversed(response["messages"]):
        if getattr(message, "type", "") == "ai" and message.content:
            content = message.content

            if isinstance(content, str):
                return content

            if isinstance(content, list):
                parts = [
                    block["text"]
                    for block in content
                    if isinstance(block, dict)
                    and block.get("type") == "text"
                    and block.get("text")
                ]
                if parts:
                    return "\n".join(parts)

    return "The agent did not return a final answer."
