import subprocess
import json
from typing import Dict


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

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
