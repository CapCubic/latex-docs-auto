#!/usr/bin/env python3
import json
from jinja2 import Environment, FileSystemLoader

def load_metadata(metadata_path):
    with open(metadata_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def render_template(template_dir, template_file, context):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)
    return template.render(context)

def main():
    metadata_file = 'metadata.json'
    template_dir = '.'  # Assumes 'template.tex' is in the current directory
    template_file = 'template.tex'
    output_file = 'output/documentation.tex'

    metadata = load_metadata(metadata_file)
    rendered_tex = render_template(template_dir, template_file, metadata)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(rendered_tex)

    print(f"Documentation generated successfully and saved to {output_file}")

if __name__ == '__main__':
    main()