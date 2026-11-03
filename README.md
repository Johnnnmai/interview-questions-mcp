# Interview Questions MCP Server

> Maintained version: [ai-interview-questions-mcp](https://github.com/Johnnnmai/ai-interview-questions-mcp) (install this one).

**Free:** [Check your interview answer](https://johnnnmai.github.io/ai-engineer-interview-questions/answer-check/?utm_source=github&utm_medium=readme&utm_campaign=interview-questions-mcp)  |  **Weekly drills:** [Interview Pass, $19/mo](https://buy.stripe.com/14AeVc4Wv7ita7O1Si5kk0j?utm_source=github&utm_medium=readme&utm_campaign=interview-questions-mcp)

An MCP server that gives your AI assistant access to curated AI Engineer interview questions with scoring rubrics. Practice directly in Claude Desktop, Cursor, or any MCP-compatible client.

## Tools

| Tool | Description |
|------|-------------|
| `list_topics()` | List all question topics with counts and difficulty levels |
| `get_question(topic, level)` | Get a random question with 3 scoring points. Levels: `junior`, `mid`, `senior` |
| `self_check_link()` | Get the link to the free answer self-checker |

## Topics

- **rag** — Retrieval-Augmented Generation
- **transformers** — Transformer Architecture
- **agents** — AI Agents
- **fine-tuning** — Fine-Tuning & Training
- **inference** — LLM Inference & Optimization
- **embeddings** — Embeddings & Vector Search
- **safety** — LLM Safety & Reliability
- **prompting** — Prompting Techniques

## Install

Requires Python 3.10+ and `uv` (or `pip`).

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "interview-questions": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/Johnnnmai/interview-questions-mcp", "interview-questions-mcp"]
    }
  }
}
```

Or clone and run locally:

```json
{
  "mcpServers": {
    "interview-questions": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/interview-questions-mcp", "python", "server.py"]
    }
  }
}
```

### Cursor

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "interview-questions": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/Johnnnmai/interview-questions-mcp", "interview-questions-mcp"]
    }
  }
}
```

## Usage

Ask your AI assistant:

- "List interview topics" → calls `list_topics()`
- "Give me a senior RAG question" → calls `get_question(topic="rag", level="senior")`
- "Where can I check my answer?" → calls `self_check_link()`

Every response includes a link to the free self-grading tool.

## Full kit

**[AI Engineer Interview Playbook](https://sirjohnnymai.gumroad.com/l/xzptir?utm_source=github&utm_medium=mcp_readme&utm_campaign=line27_20261101)** — 200+ questions with model answers, system design templates, and scoring rubrics.

## License

MIT
