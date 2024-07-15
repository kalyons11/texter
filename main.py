import datetime
import subprocess

import send


def get_git_revision_short_hash() -> str:
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()

send.send(get_git_revision_short_hash())
