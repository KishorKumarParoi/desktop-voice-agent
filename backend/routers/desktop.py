"""
FastAPI Router for Desktop Voice Assistant.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from backend.desktop_engine import (
    desktop_engine,
    DesktopCommandResponse,
    SystemMetrics
)
from backend.core.tts import generate_speech

router = APIRouter(prefix="/api/desktop", tags=["Desktop Assistant"])


class CommandRequest(BaseModel):
    query: str
    tts_provider: Optional[str] = "browser"


@router.get("/metrics", response_model=SystemMetrics)
def get_system_telemetry():
    return desktop_engine.get_system_metrics()


@router.post("/execute", response_model=DesktopCommandResponse)
def execute_desktop_command(req: CommandRequest):
    return desktop_engine.process_command(req.query)
