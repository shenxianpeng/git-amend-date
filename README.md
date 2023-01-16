# git-amend-date

[![main](https://github.com/shenxianpeng/git-amend-date/actions/workflows/main.yml/badge.svg)](https://github.com/shenxianpeng/git-amend-date/actions/workflows/main.yml)

Amend git commit date from work time to personal time.

## Usage

### Running as pre-commit hook

```yaml
- repo: https://github.com/shenxianpeng/git-amend-date
  rev: the tag or revision
  hooks:
  - id: git-amend-date
```

You can pass parameter to specify `--start-time`, `--end-time` and `--overtime`.

By default `--start-time=09:00`, `--end-time=18:00`, `--overtime=False`.

For [996](https://github.com/996icu/996.ICU) developers :)

```yaml
- repo: https://github.com/shenxianpeng/git-amend-date
  rev: the tag or revision
  hooks:
  - id: git-amend-date
    args: [--start-time=09:00, --end-time=21:00, --overtime=True]
```

### Running as CLI

```bash
pip install git+https://github.com/shenxianpeng/git-amend-date.git@main

$ git-amend-date -h
usage: git-amend-date [-h] [--start-time START_TIME] [--end-time END_TIME] [--overtime OVERTIME]

optional arguments:
  -h, --help            show this help message and exit
  --start-time START_TIME
                        workday start time. default is 09:00.
  --end-time END_TIME   workday end time. default is 18:00:00.
  --overtime OVERTIME   work overtime on weekends. default is False.
```

## Have question or feedback?

To provide feedback (requesting a feature or reporting a bug) please post to [issues](https://github.com/shenxianpeng/git-amend-date/issues).
