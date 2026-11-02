#!/usr/bin/env python3
"""AI Engineer Interview Questions — MCP Server (stdio transport)."""

import json
import random
import sys
from pathlib import Path

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print(
        "Missing dependency: pip install mcp[cli]",
        file=sys.stderr,
    )
    sys.exit(1)

DATA_FILE = Path(__file__).parent / "questions.json"
with open(DATA_FILE, encoding="utf-8") as f:
    DATA = json.load(f)

SELF_CHECK_URL = (
    "https://johnnnmai.github.io/ai-engineer-interview-questions/answer-check/"
    "?utm_source=mcp&utm_medium=tool&utm_campaign=line27_20261101"
)

CTA = f"\n\n---\nCheck your answer with our free self-grader: {SELF_CHECK_URL}"

mcp = FastMCP("interview-questions")


@mcp.tool()
def list_topics() -> str:
    """List all available interview question topics and the number of questions in each."""
    lines = []
    for key, topic in DATA["topics"].items():
        count = len(topic["questions"])
        levels = sorted({q["level"] for q in topic["questions"]})
        lines.append(f"- {key}: {topic['name']} ({count} questions, levels: {', '.join(levels)})")
    lines.append(CTA)
    return "\n".join(lines)


@mcp.tool()
def get_question(topic: str, level: str = "junior") -> str:
    """Get an interview question with scoring rubric.

    Args:
        topic: Topic key from list_topics (e.g. 'rag', 'transformers', 'agents').
        level: Difficulty — 'junior', 'mid', or 'senior'. Defaults to 'junior'.
    """
    if topic not in DATA["topics"]:
        available = ", ".join(DATA["topics"].keys())
        return f"Unknown topic '{topic}'. Available: {available}"

    questions = [
        q for q in DATA["topics"][topic]["questions"] if q["level"] == level
    ]
    if not questions:
        levels = sorted({q["level"] for q in DATA["topics"][topic]["questions"]})
        return f"No {level}-level questions for '{topic}'. Available levels: {', '.join(levels)}"

    q = random.choice(questions)
    points = "\n".join(f"  {i+1}. {p}" for i, p in enumerate(q["scoring_points"]))
    return (
        f"**{q['question']}**\n"
        f"Level: {q['level']}\n\n"
        f"Scoring points:\n{points}"
        f"{CTA}"
    )


@mcp.tool()
def self_check_link() -> str:
    """Get the link to the free AI Engineer interview answer self-checker."""
    return (
        f"Free answer self-checker: {SELF_CHECK_URL}\n\n"
        "Paste your answer to get instant feedback on completeness and accuracy."
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
