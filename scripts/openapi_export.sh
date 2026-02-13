#!/usr/bin/env bash
set -euo pipefail
python - <<'PY'
from app.main import app
import json
print(json.dumps(app.openapi(), indent=2))
PY
