#!/usr/bin/env python3
"""One line to stop the scroll — make.fun bounty entry.

The entry is a single line (141 characters) written to make a stranger
stop scrolling and smile. The program prints the entry to stdout.

Python 3.13, standard library only, fully deterministic: no network,
no clock, no randomness.
"""

import os
import sys

# The entry itself: exactly one line, 141 characters, no leading or
# trailing whitespace. This text must not change.
ENTRY = (
    "You scrolled past 200 strangers to find this one, so here's your "
    "prize: you're doing better than you think \u2014 and yes, the dog "
    "video can wait."
)

MIN_LENGTH = 1
MAX_LENGTH = 200


def check_entry(text: str) -> None:
    """Raise ValueError unless *text* is a valid single-line entry.

    Valid means: between MIN_LENGTH and MAX_LENGTH characters, no
    newline or carriage return anywhere, and no leading or trailing
    whitespace.
    """
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(char) < 0x20 or ord(char) == 0x7F for char in text):
        raise ValueError("entry must not contain control characters")


def pick_output_directory() -> str:
    """Choose a writable output directory.

    Prefer ``$MAKEFUN_OUTPUT`` when set, otherwise ``/output``; if
    neither can be created or written to, fall back to ``./output``
    next to the working directory.
    """
    candidates = [os.environ.get("MAKEFUN_OUTPUT"), "/output"]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            os.makedirs(candidate, exist_ok=True)
            probe = os.path.join(candidate, ".write_probe")
            with open(probe, "w", encoding="utf-8") as handle:
                handle.write("ok")
            os.remove(probe)
            return candidate
        except OSError:
            continue
    fallback = os.path.join(os.getcwd(), "output")
    os.makedirs(fallback, exist_ok=True)
    return fallback


def write_and_verify(directory: str, text: str) -> None:
    """Write *text* to ``entry.txt`` in *directory* and read it back.

    Raises OSError on a failed write and RuntimeError when the bytes
    read back do not match what was written.
    """
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    if os.path.getsize(path) != len(text.encode("utf-8")):
        raise RuntimeError("verification failed: written file size mismatch")
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise RuntimeError("verification failed: written entry does not match")


def main() -> int:
    check_entry(ENTRY)
    # Print the entry first: stdout is the authoritative output, and
    # it must succeed before anything else happens.
    print(ENTRY, flush=True)
    try:
        write_and_verify(pick_output_directory(), ENTRY)
    except (OSError, RuntimeError) as exc:
        # The file copy is a convenience only; the entry is already
        # printed, so a failed write — or a verification mismatch —
        # must not fail the run.
        print(f"warning: could not write entry.txt: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
