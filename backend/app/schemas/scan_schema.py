from enum import Enum

from pydantic import BaseModel, Field


class ScanType(str, Enum):
    quick = "quick"
    normal = "normal"
    full = "full"
    service = "service"


class ScanRequest(BaseModel):
    target: str = Field(..., min_length=1, max_length=255)
    scan_type: ScanType = ScanType.quick


class ScanResponse(BaseModel):
    status: str
    message: str
    target: str
