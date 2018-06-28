from distutils.core import setup

setup(
    name="naughty fakers",
    version="0.1.0",
    author="Chad Estioco",
    author_email="chadestioco@gmail.com",
    url="https://github.com/skytreader/naughty-fakers",
    packages=["naughty_fakers"],
    data_files=[("", "blns.json")],
    install_requires=["Faker==0.8.16"],
    license="MIT",
    description="Fakers that return naughty strings."
)
