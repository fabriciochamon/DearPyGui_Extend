from setuptools import setup, find_packages

setup(
    name="dearpygui_extend",
    version="0.1",
    packages=['dearpygui_extend'],
    install_requires=open("requirements.txt").readlines(),
    entry_points={
        "console_scripts": [
            # If your project has command-line scripts, add their entry points here, e.g.
            # "my_script=my_package.my_module:main",
        ],
    },
    python_requires=">=3.10",
    # Add metadata about your project
    author="Fabricio Chamon",
    author_email="fabricio.chamon@gmail.com",
    description="Extensions and custom widgets for Dear Py GUI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/fabriciochamon/DearPyGui_Extend",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
