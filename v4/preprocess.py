import os.path
import re
import schemata

docs_directory = 'docs'
filename = os.path.join(docs_directory,'schemata.md')

contents = open(filename).read()

def replacement(match):
    artifact_path = os.path.join(docs_directory, match.group(2))
    print(artifact_path)
    if not os.path.isfile(artifact_path):
        return match.group(0)

    code = open(artifact_path).read()
    print('read', artifact_path)
    return f'```json\n{code}\n```\n[Source]({match[2]})'

new_contents = re.sub(r'```json\s+(.*?)```\s+\[Source\]\((.*?)\)', replacement, contents, flags=re.S)


schema2types = {}


def get_schema_link(schema):
    # sourcery skip: assign-if-exp, inline-immediately-returned-variable
    # replacement_schemata = dict(cdd=schemata.CDDC,
    #                             mintkey=schemata.MKC,
    #                             blindsignature=schemata.ResponseMint)
    # schema = replacement_schemata.get(schema.__name__.lower(),schema)
    sn = schema.__name__
    if sn == 'CoinStack' or sn.startswith('Request') or sn.startswith('Response'):
        link =  f'[{sn} Message](#{sn.lower()}-message)'
    else:
        link = f'[{sn}](#{sn.lower()})'
    return link

def field_index_markdown():

    all_field_names = {}
    md = []
    for name, schema in sorted(schemata.type2schema.items()):
        fieldnames = sorted(schema._declared_fields.keys())
        # print(name)
        for fieldname in fieldnames:
            all_field_names.setdefault(fieldname,[]).append(schema)

    for fieldname, schemas in list(sorted(all_field_names.items())):
            used = ', '.join(get_schema_link(schema) for schema in schemas)
            md.append(f'- **{fieldname}**:  description\n  \n  Type: String  \n  Used in: {used}')
    return '\n  \n  \n  \n'.join(md)

# new_contents = re.sub(r'## Fields\n(.*?)## Building blocks\n',
#                       f'## Fields\n\n{field_index_markdown()}\n\n## Building blocks\n',
#                       new_contents,
#                       flags=re.S)

open(filename,'w').write(new_contents)
