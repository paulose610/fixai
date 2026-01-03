class DummyUsageMetadata:
    def __init__(self, prompt_tokens=10, response_tokens=20):
        self.prompt_token_count = prompt_tokens
        self.candidates_token_count = response_tokens


class DummyFunctionCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args


class DummyAIResponse:
    def __init__(
        self,
        text="This is a dummy AI response.",
        prompt_tokens=10,
        response_tokens=20,
        function_calls=None
    ):
        self.text = text
        self.usage_metadata = DummyUsageMetadata(
            prompt_tokens, response_tokens
        )
        self.function_calls = function_calls or []
