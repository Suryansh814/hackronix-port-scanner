import subprocess
from typing import Dict

from app.parsers.nmap_parser import NmapParser


class NmapScanner:

    @staticmethod
    def quick_scan(target: str) -> Dict:

        command = [
            "nmap",
            "-F",
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
