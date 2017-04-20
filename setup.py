from distutils.core import setup

setup(
    name="sshedit-gtk",
    version="0.0.1",
    author="Oscar Carballal Prego",
    author_email="oscar@oscarcp.com",
    packages=["."],
    include_package_data=True,
    url="http://pypi.python.org/pypi/sshedit-gtk/",
    license="LICENSE",
    description="GTK+ SSH Configuration Editor",
    install_requires=[
        "paramiko",
    ],
)
