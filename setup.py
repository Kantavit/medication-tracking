from setuptools import find_packages, setup

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

setup(
    name="med-track",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,  # To include other files, such as the static and templates directories
    zip_safe=False,
    install_requires=install_requires,
    scripts=["run-web"],
)
