from prompts.resume_prompt import resume_prompt


def test_prompt_accepts_resume_text():
    messages = resume_prompt.format_messages(
        resume_text="My name is Arjun. I know Java."
    )

    assert len(messages) > 0
    assert "My name is Arjun" in messages[-1].content


def test_prompt_instructs_model_not_to_invent_information():
    messages = resume_prompt.format_messages(
        resume_text="My name is Arjun. I know Java."
    )

    system_message = messages[0].content

    assert "Never invent missing information" in system_message