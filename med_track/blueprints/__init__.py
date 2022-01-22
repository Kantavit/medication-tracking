from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module


# all register blueprint from sub package
def register_blueprints(app):
    # iterate through the package in the current package
    package_dir = Path(__file__).resolve().parent
    for (_, module_name, _) in iter_modules([package_dir]):
        module = import_module(f"{__name__}.{module_name}")
        app.register_blueprint(module.bp)
        # print(module, module.bp)
