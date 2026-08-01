import subprocess
from typing import Dict

from app.parsers.nmap_parser import NmapParser


class NmapScanner:

    SCAN_COMMANDS = {
        "quick": ["nmap", "-F"],
        "normal": ["nmap"],
        "full": ["nmap", "-p-"],
        "service": ["nmap", "-sV"],
    }

    @classmethod
    def run_scan(cls, target: str, scan_type: str) -> Dict:

        command = cls.SCAN_COMMANDS.get(scan_type)

        if command is None:
            return {
                "status": "error",
                "message": f"Unknown scan type: {scan_type}"
            }

        command = command + [
            "-oX",
            "-",
            target
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return {
                "status": "error",
                "message": result.stderr
            }

        return NmapParser.parse(result.stdout)
