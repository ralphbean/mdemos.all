
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name="mdemos.all",
    version="0.1.2",
    url="http://moksha.fedorahosted.org",
    description="Meta-package to install all Moksha demo apps",
    long_description="",
    author="Ralph Bean",
    author_email="rbean@redhat.com",
    license="ASL 2.0",
    packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        "mdemos.menus",
        "mdemos.metrics",
        "mdemos.chat",
        "mdemos.server",
        #"mdemos.feeds",  # <-- this one doesn't actually work.
    ],
)
