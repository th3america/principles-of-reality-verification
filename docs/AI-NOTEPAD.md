# AI Notepad as a Reality Verification Surface

AI Notepad is an example of a mechanism built from the framework. It is not the
framework itself and it is not merely a generic file manager.

Its useful behavior is to make mixed conversation evidence easy to capture and
later parse:

```slangs
copy chat or other source
→ paste into note
→ preserve text + formatting + embedded pictures
→ package content + manifest
→ retain speaker/presence boundaries
→ make counts and contents inspectable
→ support later AI intake and reality checks
```

## Why the package matters

A `.ainote` can contain a document body and a manifest describing measurable
properties such as words, characters, lines, and images. The exact container
format is an implementation choice. The verification value comes from keeping
the captured body, embedded media, and count metadata together so later claims
can be checked against the same bounded artifact.

## Presence tokens are structural

Presence marks such as `🔸` and `🐾` are not merely decoration when a source
uses them to identify speakers. Combined with spacing, timestamps, and status
boundaries, they help divide turns and preserve attribution.

```slangs
prior output ends
→ visible gap / time / status boundary
→ user input
→ presence token
→ attributed response begins
```

The parser must learn the source grammar rather than assume every emoji is a
speaker marker. A token is evidence of attribution only within the convention
that defines it.

## Verification uses

An AI or human can use the package to check:

- whether the complete capture opened;
- whether embedded pictures are present;
- whether manifest counts match the captured body under the same counting
  rules;
- where speaker boundaries occur;
- whether a quoted passage belongs to the user, an assistant, or quoted
  external material;
- whether later summaries omit, merge, or misattribute important turns.

## Limits

The note verifies capture state, not the truth of every statement inside it.
Presence tokens aid attribution but do not independently prove identity. Word
and character counts require declared counting rules. A complete capture can
still contain false claims, and a correct summary still needs a trace back to
the relevant source spans.
