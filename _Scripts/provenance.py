#!/usr/bin/env python3
"""Derive stable provenance tags from recorded host and model values."""

import re


PROVENANCE_PREFIXES = ("host/", "ai/", "model/")


def tag_slug(value):
    """Return a lowercase Obsidian-safe tag segment."""
    slug = re.sub(r"[^a-z0-9]+", "-", str(value or "").strip().lower()).strip("-")
    return slug or "unknown"


def ai_family(model):
    """Classify a recorded model name without guessing from its host."""
    value = str(model or "").strip().lower()
    boundary = r"[-_ /]"
    if re.search(rf"(^|{boundary})gpt({boundary}|$)", value) or re.search(rf"(^|{boundary})o[134]({boundary}|$)", value):
        return "gpt"
    for family in ("claude", "grok", "gemini"):
        if re.search(rf"(^|{boundary}){family}({boundary}|$)", value):
            return family
    return "unknown"


def provenance_tags(host, model):
    """Return host, AI-family, and exact-model tags in a stable order."""
    return [
        f"host/{tag_slug(host)}",
        f"ai/{ai_family(model)}",
        f"model/{tag_slug(model)}",
    ]


def merge_provenance_tags(tags, host, model):
    """Replace stale provenance tags while preserving unrelated tag order."""
    kept = [
        tag for tag in tags
        if not any(tag.lower().startswith(prefix) for prefix in PROVENANCE_PREFIXES)
    ]
    return kept + provenance_tags(host, model)
