import os.path
import re
filename = 'OpenCoin.md'

contents = open(filename).read()

def replacement(match):
    artifact_path = match.group(2)
    if not os.path.isfile(artifact_path):
        return match.group(0)

    code = open(artifact_path).read()
    return f'```json\n{code}\n```\n[Source]({artifact_path})'

new_contents = re.sub(r'```json\s+(.*?)```\s+\[Source\]\((.*?)\)', replacement, contents, flags=re.S)
open(filename,'w').write(new_contents)