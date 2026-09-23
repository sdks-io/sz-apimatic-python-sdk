"""Per-call request options -- the SDK's one override channel.

Every endpoint takes an optional ``request_options``, so a caller can override request-scoped
behaviour for a single call without re-configuring the client::

    client.body_params.send_long(5, request_options={"timeout": 5.0})

One bundled parameter rather than a keyword per knob. That is what keeps the set of names a
generated endpoint reserves at exactly one, however many options are added later: a new option is a
field here and collides with nobody's parameter.

Accepted either typed or dict-shaped, the same either-spelling convention the model input companions
use. :meth:`RequestOptions.coerce` is the one place the dict form is resolved, so the two spellings
cannot produce different requests.

A validated model rather than a plain frozen dataclass, because of who supplies the value: this is
caller input, so its constraint and its unknown-key rejection are declared here rather than
hand-written, exactly as they are for the configuration models. What the runtime *builds* --
including the resolved timeout that reaches a transport on :class:`HttpRequest` -- stays a plain
dataclass field, so no model crosses the transport boundary."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Final, TypeAlias

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import NotRequired, TypedDict


class RequestOptions(BaseModel):
    """Overrides that apply to a single request.

    ``frozen`` matches every other value type in the runtime; ``extra="forbid"`` rejects a
    misspelled option that reached here without a type checker having seen the call."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    timeout: float | None = Field(default=None, gt=0)
    """Seconds to wait for this one request. ``None`` leaves the client's own timeout in force."""

    extra_headers: Mapping[str, str] | None = None
    """Headers added to this one request, winning over both the API's and the endpoint's own."""

    @classmethod
    def coerce(cls, options: RequestOptionsOrDict | None) -> RequestOptions:
        """Return ``options`` as a :class:`RequestOptions`, dict-shaped input included.

        An instance passes straight through -- it validated itself when it was built -- and ``None``
        yields the shared empty options rather than ``None`` itself, so the path every call that
        overrides nothing takes neither validates nor allocates, and every read downstream stays
        unconditional as fields are added.

        Everything else is validated, an empty mapping and a falsy value of the wrong type included.
        ``None`` is the only short circuit deliberately: a caller no type checker saw is exactly who
        this validation is for, and absorbing their ``False`` or ``()`` as "no overrides" would
        leave them believing an override took effect.

        Args:
            options: The caller's per-call overrides, in either spelling, or ``None`` for none.

        Returns:
            A validated :class:`RequestOptions`; the shared empty instance when ``options`` is
            ``None``.

        Raises:
            ValidationError: If ``options`` carries an unknown key or an out-of-range value. It
                subclasses ``ValueError``, so a caller catching that still covers this."""
        if isinstance(options, cls):
            return options
        if options is None:
            return _NO_OPTIONS
        return cls.model_validate(options)


class RequestOptionsDict(TypedDict):
    """The dict-shaped spelling of :class:`RequestOptions`, mirroring it field for field.

    Closed and typed per key, which is what makes ``request_options={"timeuot": 1}`` a type error at
    the call site rather than a surprise at runtime."""

    timeout: NotRequired[float | None]
    extra_headers: NotRequired[Mapping[str, str] | None]


RequestOptionsOrDict: TypeAlias = RequestOptions | RequestOptionsDict
"""What an endpoint accepts: the typed options, or a dict carrying the same keys.

Aliased rather than spelled out at each call site -- unlike a model and its companion, which a
generator writes as a pair per schema, there is exactly one options type, so a single alias is what
keeps every emitted signature on one line instead of four."""

_NO_OPTIONS: Final = RequestOptions()
"""The empty options, built once -- the default path for every call that overrides nothing."""
