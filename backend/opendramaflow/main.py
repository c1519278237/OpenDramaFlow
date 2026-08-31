from fastapi import FastAPI

app = FastAPI(title="OpenDramaFlow API")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
