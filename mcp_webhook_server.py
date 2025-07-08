# mcp_webhook_server.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.post("/gitlab-webhook")
async def gitlab_webhook(request: Request):
    payload = await request.json()
    object_kind = payload.get("object_kind")
    attrs = payload.get("object_attributes", {})
    
    if object_kind != "merge_request":
        return {"status": "ignored", "reason": "not a merge request"}

    if attrs.get("state") != "merged":
        return {"status": "ignored", "reason": "not merged yet"}

    # Extract key fields
    mr_title = attrs.get("title")
    source_branch = attrs.get("source_branch")
    target_branch = attrs.get("target_branch")
    merge_commit_sha = attrs.get("merge_commit_sha")
    repo_url = payload.get("project", {}).get("git_http_url")

    logging.info(f"[Webhook] Merge Request Merged: {mr_title}")
    logging.info(f" - Source: {source_branch} → Target: {target_branch}")
    logging.info(f" - SHA: {merge_commit_sha}")
    logging.info(f" - Repo: {repo_url}")

    # Store to DB / queue / process immediately
    # For now, we just log or could write to a local file
    with open("latest_merge_event.json", "w") as f:
        import json
        json.dump(payload, f, indent=2)

    return {"status": "received", "merge_commit_sha": merge_commit_sha}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
