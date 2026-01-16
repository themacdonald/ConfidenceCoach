import subprocess
import sys
from pathlib import Path


def test_cli_demo(tmp_path):
    out_dir = tmp_path / "reports"
    out_file = out_dir / "report.json"
    result = subprocess.run([sys.executable, "-m", "confidencecoach.cli", "--demo", "--out", str(out_file)], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Wrote" in result.stdout
    assert out_file.exists()
