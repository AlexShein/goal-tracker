import json
import os
from typing import List

CORS_ALLOWED_ORIGINS: str = os.environ.get("CORS_ALLOWED_ORIGINS")  # type:ignore
DB_ADDR: str = os.environ.get("DB_ADDR")  # type:ignore
DB_PASS: str = os.environ.get("DB_PASS")  # type:ignore
DB_USER: str = os.environ.get("DB_USER")  # type:ignore

missing_env_vars = []
for var_name, env_var in [
    # ("CORS_ALLOWED_ORIGINS", CORS_ALLOWED_ORIGINS),
    ("DB_ADDR", DB_ADDR),
    ("DB_PASS", DB_PASS),
    ("DB_USER", DB_USER),
]:
    if not env_var:
        missing_env_vars.append(var_name)

if missing_env_vars:
    raise RuntimeError(f"Following environment variables are required, but missing: {missing_env_vars}")

CORS_ALLOWED_ORIGINS_LIST: List[str] = json.loads(CORS_ALLOWED_ORIGINS) if CORS_ALLOWED_ORIGINS else []
