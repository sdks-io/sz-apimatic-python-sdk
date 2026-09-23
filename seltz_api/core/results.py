"""The result of one API call, as a value rather than an exception.

``ApiResult`` is a tagged union: a call yields exactly one of :class:`Success` or :class:`Failure`,
never both and never neither, so which one you hold is a fact the type checker can see. Narrow it
with ``match`` or ``isinstance`` and the payload or error comes with it:

    match client.body_params.with_raw_response.send_model(employee):
        case Success(payload=confirmation):
            ...
        case Failure(error=err):
            ...

Both variants are frozen dataclasses, so pattern matching needs nothing added. ``.unwrap()`` is the
shortcut for callers that would rather not branch -- it returns the payload or raises.

:class:`RawError` lives here too: it is the error type a :class:`Failure` carries when the operation
does not document the status that came back."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Generic, NoReturn, TypeAlias, TypeVar

from .exceptions import ApiError
from .transport import HttpResponse

T = TypeVar("T")
E = TypeVar("E")


@dataclass(frozen=True, slots=True)
class Success(Generic[T]):
    """A successful (2xx) API call carrying the decoded ``payload``."""

    payload: T
    response: HttpResponse

    def unwrap(self) -> T:
        """Collapse this result to its parsed value.

        Returns:
            The decoded payload. This variant never raises."""
        return self.payload


@dataclass(frozen=True, slots=True)
class Failure(Generic[E]):
    """A failed (non-2xx) API call carrying the decoded error body ``error``.

    ``error`` is the typed error payload directly (a union of the operation's
    documented schemas, or :class:`RawError` for an unmapped status) -- not a wrapper."""

    error: E
    response: HttpResponse

    def unwrap(self) -> NoReturn:
        """Collapse this result to its parsed value, which for a failure means raising.

        Raises:
            ApiError: Always, carrying this result's ``error`` and ``response``."""
        raise ApiError(error=self.error, response=self.response)


# One call yields exactly one of these; narrow with ``match`` or ``isinstance``,
# or collapse to the parsed value with ``.unwrap()``.
ApiResult: TypeAlias = Success[T] | Failure[E]


@dataclass(frozen=True, slots=True)
class RawError:
    """Undecoded fallback body (unmapped status / no declared schema).

    Wraps the raw response so the status and bytes are available and decoded on
    demand. Constructed directly -- ``RawError(response)``."""

    response: HttpResponse

    @property
    def status_code(self) -> int:
        return self.response.status_code

    @property
    def content(self) -> bytes:
        return self.response.content

    def text(self, encoding: str = "utf-8") -> str:
        """Decode the undecoded body as text, for a log line or a diagnostic.

        Args:
            encoding: Character encoding to decode with.

        Returns:
            The body as text, undecodable bytes replaced rather than raising."""
        return self.response.text(encoding)

    def json(self) -> Any:
        """Parse the undecoded body as JSON.

        Returns:
            Whatever the body parses to.

        Raises:
            ValueError: If the body is not valid JSON."""
        return self.response.json()

    def __repr__(self) -> str:
        # Identify the response by status only -- the (undecoded, possibly large,
        # binary, or sensitive) body and the headers/request are deliberately kept
        # out of the string form. Read the body on demand via ``text``/``json``.
        return f"{type(self).__name__}(status_code={self.status_code})"
