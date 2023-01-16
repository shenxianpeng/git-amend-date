from __future__ import annotations

import argparse
import subprocess
from datetime import datetime, date

TIME_FMT = "%H:%M:%S"


def git_commit_amend_date(datetime: datetime) -> str:
    """Update git commit date with new datetime."""
    commands = ['git', 'commit', '--amend', '--no-edit', '--date', f"{datetime}"]
    result = subprocess.run(
        commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8'
    )
    if result.returncode == 0 and result.stdout is not None:
        return result.stdout
    elif result.stderr != '':
        return result.stderr
    else:
        return ''


def get_commit_time(start_time: datetime, end_time: datetime, overtime: bool):
    """Check start_time, end_time, and overtime,
    then decide if need to update commit time.
    """
    time_str = datetime.now().strftime(TIME_FMT)
    current_time = datetime.now().strptime(time_str, TIME_FMT)
    today = date.today()
    weekday = datetime.today().weekday()
    current_datetime = datetime.combine(today, current_time.time())

    offset = (end_time - start_time) / 2
    start_offset = current_time - start_time
    end_offset = end_time - current_time

    if not overtime and weekday in (5, 6):
        # commit on weekends and not overtime.
        return current_datetime
    if current_time >= end_time:
        # commit after get off work on weekday
        return current_datetime
    if start_offset >= end_offset:
        # commit in the afternoon on weekday
        return datetime.combine(today, (end_time + (offset - end_offset)).time())
    else:
        # commit in the morning on weekday
        return datetime.combine(today, (start_time - (offset - start_offset)).time())


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--start-time',
        default="09:00:00",
        type=str,
        help="work start time. default is 09:00.",
        required=False,
    )

    parser.add_argument(
        '--end-time',
        default="18:00:00",
        type=str,
        help="work end time. default is 18:00:00.",
        required=False,
    )

    parser.add_argument(
        '--overtime',
        default=False,
        type=bool,
        help="work overtime on weekends. default is False.",
        required=False,
    )

    args = parser.parse_args()
    start_time = datetime.strptime(args.start_time, TIME_FMT)
    end_time = datetime.strptime(args.end_time, TIME_FMT)
    overtime = args.overtime

    if start_time > end_time:
        raise argparse.ArgumentTypeError(
            start_time,
            end_time,
            "end_time must later than start_time."
        )
    commit_time = get_commit_time(start_time, end_time, overtime)
    print(git_commit_amend_date(commit_time))


if __name__ == "__main__":
    main()
