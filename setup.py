from distutils.core import setup

setup(
    name="octodon",
    version="0.1.0",
    author="Oscar Carballal Prego",
    author_email="oscar.carballal@protonmail.com",
    packages=["."],
    include_package_data=True,
    url="http://pypi.python.org/pypi/octodon/",
    license="LICENSE",
    description="GTK+ SSH Configuration Editor",
    install_requires=[
        "paramiko",
    ],
)
