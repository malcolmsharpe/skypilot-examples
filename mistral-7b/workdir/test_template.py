# Run to see how the template formats the system message.
from jinja2 import Template

template_path = 'template_mistral_7b_system.jinja'
template = Template(open(template_path).read())

def raise_exception(msg):
    raise ValueError(msg)

def try_render(messages):
    try:
        rendered = template.render(bos_token='<s>', eos_token='</s>', raise_exception=raise_exception, messages=messages)
        print(f'SUCCESS: {repr(rendered)}')
    except ValueError as e:
        print(f'FAIL: {e}')

messages_system = [
    {'role': 'system', 'content': 'lorem'},
    {'role': 'user', 'content': 'ipsum'},
    {'role': 'assistant', 'content': 'dolor'},
    {'role': 'user', 'content': 'sit'},
]

try_render(messages_system)
