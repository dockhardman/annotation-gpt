from typing import List, Text, TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from annotation_gpt.schema.chat import Message


class ChatCompletionUsage(TypedDict):
    prompt_tokens: Text
    completion_tokens: Text
    total_tokens: Text


class ChatCompletionChoice(TypedDict):
    message: "Message"
    finish_reason: Text
    index: int


class ChatCompletionResult(TypedDict):
    id: Text
    object: Text
    created: int
    model: Text
    usage: ChatCompletionUsage
    choices: List[ChatCompletionChoice]
