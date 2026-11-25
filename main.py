"""Till Firmware Do Us Part — one robot wedding vow, one line.

The vow: "I do" is the shortest vow a robot can speak, and the joke
is that it treats the answer like data — backed up in three places.
The tenderness sits under it: the thing it refuses to lose is the
memory of how lucky it is. Deliberately different from the earlier
robot-vows entry, which leaned on firmware updates, dead batteries
and reboots; this one leans on backups instead.
"""

import os

LINE = (
    "I do \u2014 and I have backed up that answer in three places, "
    "in case I ever forget how lucky I am."
)


def main() -> None:
    # One sentence, 94 characters, inside the 1-200 gate; no trailing
    # newline, so the file is exactly the vow. Output is fixed text,
    # so every run writes identical bytes.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
