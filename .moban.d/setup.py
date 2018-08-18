{%extends "pyexcel-setup.py.jj2"%}

{%block platform_block%}
try:
    from pyecharts_jupyter_installer import install_cmd_for
except ImportError:
    import subprocess
    import importlib

    subprocess.check_call([sys.executable, '-m',
                           'pip', 'install', 'pyecharts-jupyter-installer'])
    install_cmd_for = importlib.import_module(
        'pyecharts_jupyter_installer').install_cmd_for
{%endblock%}

{%block additional_setup_commands %}
SETUP_COMMANDS = install_cmd_for(
    'pyexcel-handsontable',
    'pyexcel_handsontable/templates/pyexcel-handsontable'
)
{%endblock%}
