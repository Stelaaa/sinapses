import json
from urllib import error, request

from .provider import LLMProvider


class OllamaProvider(LLMProvider):
    """Implementação do LLMProvider para o Ollama local."""

    def __init__(
        self,
        model: str,
        api_url: str = "http://localhost:11434",
    ) -> None:
        self.model = model
        self.api_url = api_url.rstrip("/")

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        data = json.dumps(payload).encode("utf-8")

        http_request = request.Request(
            f"{self.api_url}/api/generate",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with request.urlopen(http_request, timeout=120) as response:
                response_data = json.loads(response.read().decode("utf-8"))
        except error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(
                f"Erro HTTP do Ollama ({exc.code}): {body}"
            ) from exc
        except error.URLError as exc:
            raise RuntimeError(
                f"Não foi possível conectar ao Ollama: {exc.reason}"
            ) from exc

        if "response" not in response_data:
            raise RuntimeError(
                "Resposta do Ollama não contém o campo 'response'."
            )

        return response_data["response"]
