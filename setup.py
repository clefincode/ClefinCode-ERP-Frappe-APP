from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in clefincode_erp/__init__.py
from clefincode_erp import __version__ as version

setup(
	name="clefincode_erp",
	version=version,
	description="ClefinCode ERP",
	author="Ahmad Kamaleddin",
	author_email="ahmad@clefincode.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
