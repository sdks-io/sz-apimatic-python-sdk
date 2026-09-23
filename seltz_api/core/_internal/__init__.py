"""Runtime plumbing.

Nothing here is part of the SDK's public surface: these are the pure functions the raw client calls
to turn parameters into a URL, a header mapping, and form fields. They are grouped under a private
package so this runtime's own ``__init__`` stays the whole of what generated code imports."""

__all__: list[str] = []
