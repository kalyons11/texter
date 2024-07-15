import datetime
import subprocess

import send


def get_git_revision_short_hash() -> str:
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()

current_time = datetime.datetime.now().isoformat()
send.send(f"{current_time}\n{get_git_revision_short_hash()}")
