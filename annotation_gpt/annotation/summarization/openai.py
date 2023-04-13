from typing import Optional, Text, TYPE_CHECKING

from annotation_gpt.config import logger
from annotation_gpt.schema.chat import Message
from annotation_gpt.schema.result import SummarizationResult

try:
    import openai
except ImportError:
    logger.warning(
        "Openai is not installed. Please install it by `pip install openai`."
    )

if TYPE_CHECKING:
    from openai.openai_object import OpenAIObject
    from annotation_gpt.schema.openai.result import ChatCompletionResult


class OpenaiSummarization(object):
    model = "gpt-3.5-turbo"
    system_prompt = """\
You will summarize document pasted by user.

Instructions:
- Your summary texts should be in language {language_hint}."""
    default_language_hint = "the same as that of the document"

    def __init__(self, *args, language_hint: Optional[Text] = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.language_hint = language_hint or self.default_language_hint

    def process(
        self, document: Text, language_hint: Optional[Text] = None
    ) -> SummarizationResult:
        document = document.strip()
        language_hint = language_hint or self.language_hint

        messages = [
            Message(role="system", content=self.system_prompt),
            Message(role="user", content=document),
        ]

        for message in messages:
            message["content"] = message["content"].format(language_hint=language_hint)

        chat_completion_result: "OpenAIObject" = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        chat_completion_result_dict: ChatCompletionResult = (
            chat_completion_result.to_dict_recursive()
        )

        return SummarizationResult(
            document=document,
            summary=chat_completion_result_dict["choices"][-1]["message"]["content"],
        )
