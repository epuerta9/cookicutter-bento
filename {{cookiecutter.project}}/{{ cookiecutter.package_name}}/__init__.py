import djp

@djp.hookimpl
def settings(current_settings):
    current_settings["KITCHENAI"]["{{ cookiecutter.package_name }}"] = "{{cookiecutter.package_name}}.bento.kitchen.router"