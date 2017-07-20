"""{
    "module": "command",
    "handler": "run",
    "jobparam": {"cmd"      : {"L": ["ls", "-1"]}}
}
"""

import subprocess
import logging

logging.config.fileConfig('etc/worker_logging.conf')

def simple_run(jobid, jobparam):
    """just execute the command"""
    command = []
    if "S" in jobparam["cmd"]:
        command = jobparam["cmd"]["S"].split(" ")
    elif "L" in jobparam["cmd"]:
        command = jobparam["cmd"]["L"]

    logging.info(command)
    p = subprocess.Popen(command,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    logging.info("stdout: %s", stdout)
    logging.info("stderr: %s", stderr)
