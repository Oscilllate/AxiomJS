import re
import os

# Paths (relative to this script)
BASE_DIR = os.path.dirname(__file__)

input_file = os.path.join(BASE_DIR, "module", "osc.module.js")
output_file = os.path.join(BASE_DIR, "script", "osc.js")

# Read module file
with open(input_file, "r", encoding="utf-8") as f:
    code = f.read()

# ---- Transform exports ----

# export function / const / let / var
code = re.sub(r"\bexport\s+(function|const|let|var)\b", r"\1", code)

# export default
code = re.sub(r"\bexport\s+default\s+", "", code)

# export { a, b, c }
code = re.sub(r"\bexport\s*{\s*([^}]*)\s*};?", r"", code)

# Ensure output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Write output
with open(output_file, "w", encoding="utf-8") as f:
    f.write(code)

print(f"Generated {output_file} from {input_file}")