from annotation_gpt.annotation.summarization.openai import OpenaiSummarization


def test_openai_summarization():
    openai_sum = OpenaiSummarization()
    result = openai_sum.process(
        """\
ChatGPT plugins
We’ve implemented initial support for plugins in ChatGPT. Plugins are tools designed specifically for language models with safety as a core principle, and help ChatGPT access up-to-date information, run computations, or use third-party services.""",
        language_hint="Japanese",
    )
    assert result["document"]
    assert result["summary"]
