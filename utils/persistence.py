import json, asyncio
from pathlib import Path

DATA_FILE = Path("data/tasks.json")
LOCK = asyncio.Lock()

async def load_tasks() -> list[str]:
    if not DATA_FILE.exists():
        return []
    async with LOCK:
        txt = await asyncio.to_thread(DATA_FILE.read_text)
        return json.loads(txt)

async def save_tasks(tasks: list[str]) -> None:
    DATA_FILE.parent.mkdir(exist_ok=True)
    async with LOCK:
        await asyncio.to_thread(
            DATA_FILE.write_text, json.dumps(tasks, indent=2, ensure_ascii=False)
        )
