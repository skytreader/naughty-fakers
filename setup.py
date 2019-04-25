from setuptools import setup

setup(
    name="naughties",
    version="0.1.7",
    author="Chad Estioco",
    author_email="chadestioco@gmail.com",
    packages=["naughties"],
    data_files=[(".", ["blns.json"])],
    install_requires=["Faker==1.0.5"],
    license="MIT",
    description="Fakers that return naughty strings."
)
