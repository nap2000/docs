"""
Generate the tables of the expressions page (ref-expressions.rst) from the spec that the server checks
expressions with: smapserver2/sdDAL/src/org/smap/sdal/resources/form-expressions.json

  python3 tools/expression_tables.py [spec]           write tables/*.csv
  python3 tools/expression_tables.py --check [spec]   fail if the tables differ from what the spec gives

The spec defaults to ../smapserver2 next to this repository.
"""
import csv
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_SPEC = os.path.join(HERE, "..", "smapserver2", "sdDAL", "src", "org", "smap", "sdal", "resources",
                            "form-expressions.json")


def tables(spec):
    out = {}
    for c in spec["docs"]["categories"]:
        buf = io.StringIO(newline="")
        w = csv.writer(buf, lineterminator="\r\n" if c.get("crlf") else "\n")
        w.writerow(c["header"])
        for r in spec["docs"]["rows"]:
            if r["category"] == c["id"]:
                w.writerow([r["cells"].get(h, "") for h in c["header"]][:r["count"]])
        out[c["id"]] = buf.getvalue()
    return out


def main(args):
    check = "--check" in args
    args = [a for a in args if a != "--check"]
    spec_path = args[0] if args else DEFAULT_SPEC
    with open(spec_path, encoding="utf-8") as f:
        spec = json.load(f)
    differ = []
    for name, text in tables(spec).items():
        path = os.path.join(HERE, "tables", name + ".csv")
        if check:
            current = open(path, newline="", encoding="utf-8").read() if os.path.exists(path) else None
            if current != text:
                differ.append(name)
        else:
            with open(path, "w", newline="", encoding="utf-8") as f:
                f.write(text)
    if check:
        if differ:
            print("Out of step with the spec: " + ", ".join(differ))
            return 1
        print("Tables match the spec")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
