#!/usr/bin/env python3
"""生成新的 FlyTune auth.json。密码只作为命令行参数，不落盘。"""
import argparse, hashlib, json, secrets
from datetime import datetime
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("password")
p.add_argument("valid_until", nargs="?", default="2027-12-31")
p.add_argument("--iterations", type=int, default=120000)
args = p.parse_args()
salt = secrets.token_bytes(32)
h = hashlib.pbkdf2_hmac("sha256", args.password.encode(), salt, args.iterations, 32)
auth = {
    "enabled": True,
    "algorithm": "PBKDF2WithHmacSHA256",
    "iterations": args.iterations,
    "salt": salt.hex(),
    "passwordHash": h.hex(),
    "validUntil": f"{args.valid_until}T23:59:59+08:00",
    "message": "输入云端授权密码，解锁风扇转速与 245 超频档。",
}
Path("cloud/auth.json").write_text(json.dumps(auth, ensure_ascii=False, indent=2))
print("updated cloud/auth.json", datetime.now().isoformat(timespec="seconds"))
