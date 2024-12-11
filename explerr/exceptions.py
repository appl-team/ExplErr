import traceback
from typing import Optional

import appl
from appl import SystemMessage, gen, ppl
from appl.compositor import Tagged


@ppl()
def get_explanation(
    traceback: str, error_msg: str = "", extra_msg: str = "", max_tokens: int = 500
) -> str:
    """Get explanation of the error using LLM.

    Args:
        traceback: The traceback of the error.
        error_msg: The error message.
        extra_msg: The extra message.
        max_tokens: The maximum number of tokens to generate.

    Returns:
        The explanation of the error.
    """

    SystemMessage("""You are an expert at explaining Python errors. Provide a very brief,
    clear explanation of the error and suggest possible solutions. Focus on being
    concise and practical.""")

    if error_msg:
        f"Error Message: {error_msg}"
    if extra_msg:
        f"Extra Message: {extra_msg}"

    with Tagged("stack_trace"):
        traceback

    "Please explain this error briefly and suggest how to fix it."

    return str(gen(max_tokens=max_tokens))


class ExceptionWithExplanation(Exception):
    def __init__(
        self, original_exception: Optional[Exception] = None, message: str = ""
    ):
        appl.init()  # init appl here if not initialized
        if original_exception is not None:
            error_msg = (
                f"[{original_exception.__class__.__name__}] {original_exception}"
            )
            extra_msg = message
            tb_str = "".join(traceback.format_tb(original_exception.__traceback__))
        else:
            error_msg = message
            extra_msg = ""
            tb_str = "".join(traceback.format_stack()[:-1])  # Exclude current frame

        try:
            explanation = get_explanation(tb_str, error_msg, extra_msg)
        except Exception as e:
            explanation = f"Failed to get explanation from AI with error: {str(e)}"

        # Combine original error with AI explanation
        full_message = f"{error_msg}\n\nExplanation by AI: {explanation}"
        super().__init__(full_message)
