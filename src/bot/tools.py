from enum import Enum


class State(Enum):
    STATE_FIRST = 1
    STATE_SECOND = 2
    STATE_THIRD = 3


"""
Format dictionary context:
{
    message.chat.id: State.type_of_state
}
"""
context = {}


def deletion_from_context(chat_id):
    if chat_id in context:
        del context[chat_id]
