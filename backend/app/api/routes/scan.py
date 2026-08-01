from fastapi import APIRouter, HTTPException

from app.schemas.scan_schema import ScanRequest
from app.services.nmap_service import NmapScanner
from app.utils.validator import is_valid_target

router = APIRouter()


@router.post("/scan")
def scan_target(request: ScanRequest):

    if not is_valid_target(request.target):
        raise HTTPException(
            status_code=400,
            detail="Invalid target"
        )

    result = NmapScanner.run_scan(
    target=request.target,
    scan_type=request.scan_type.value
)

    return result
