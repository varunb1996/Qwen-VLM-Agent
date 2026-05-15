from agents.summarizer_agent import summarizer_agent


def reasoning_agent(response):

    summarized_response = summarizer_agent(
        response
    )

    return summarized_response