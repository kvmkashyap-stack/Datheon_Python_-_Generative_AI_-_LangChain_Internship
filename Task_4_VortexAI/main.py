from agent.executor import ask_agent, build_agent

def main():
    print("=" * 50)
    print("NexusAI - Multi-Tool Autonomous AI Agent")
    print("Tools: Web Search | Calculator | File Reader")
    print("Type 'exit' to quit.")
    print("=" * 50)

    try:
        agent = build_agent()
    except Exception as exc:
        print(f"Could not initialize NexusAI: {exc}")
        return

    while True:
        try:
            question = input("\nYou: ").strip()

            if question.lower() in {"exit", "quit"}:
                print("NexusAI: Goodbye!")
                break

            if not question:
                continue

            answer = ask_agent(agent, question)
            print(f"\nNexusAI: {answer}")

        except KeyboardInterrupt:
            print("\nNexusAI: Goodbye!")
            break
        except Exception as exc:
            print(f"\nNexusAI encountered an error: {exc}")


if __name__ == "__main__":
    main()
