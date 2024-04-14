from httpx import post
from pydantic import BaseModel

from unit_testing_disciplines.secrets.get_secret import get_secret


class SendResult(BaseModel):
    id: str  # The ID for the message
    status: str  # The status of the message (e.g. sent, queued, failed).


def send(protocol: str, to: str, from_: str, message: str) -> SendResult:
    text_api_key = get_secret("text_api_key")
    result = post(
        "https://t-e-x-t.example.com/send",
        headers={"X-API-KEY": text_api_key},
        json={
            "protocol": protocol,
            "to": to,
            "from": from_,
            "message": message,
        },
    )
    result.raise_for_status()
    response = result.json()
    return SendResult(
        id=response["id"],
        status=response["status"],
    )