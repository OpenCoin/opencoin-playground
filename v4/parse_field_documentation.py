import re
import sys
from pprint import pprint

field_filename = 'docs/fields.md'
field_text = open(field_filename).read()


def get_field_data(text):
    out = {}
    data = re.findall(r'### ([^\n]+)\n([^\n]+?)\n\s*(.*?)Type: ([^\n]+)\nUsed in: ([^\n]+)', text, flags=re.S)
    for field_name, title, description, typ, uses in data:
        out[field_name] = dict(
                title=title.strip(),
                description=description.strip().replace('\n  ', ' '),
                typ=typ.strip(),
                uses=uses.strip())
    return out

field_data = get_field_data(field_text)

def replace_field_use(match):
    field_name = match[2]
    data = field_data[field_name]
    return f'{match[1]}- **[{field_name}](fields.md#{field_name})**: {data["title"]}  *({data["typ"]})*\n'

schema_filename = 'docs/schemata.md'
schema_text = open(schema_filename).read()
new_text = re.sub(r'(\s*)- \*\*\[(.*?)\]\(.*?\)\*\*:.*?\n',replace_field_use, schema_text)
open(schema_filename,'w').write(new_text)

