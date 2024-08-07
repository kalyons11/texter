import datetime
import subprocess

import send


def get_git_revision_short_hash() -> str:
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()

current_time_iso = datetime.datetime.now().isoformat()
current_revision_short_hash = get_git_revision_short_hash()

send.send(f"Hello there - {current_revision_short_hash}")
