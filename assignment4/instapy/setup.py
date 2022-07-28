from distutils.core import setup
import setuptools

setup(
	name="instapy",
	version="1.1",
	author="Ada W. Ravn",
	author_email="adalw@ifi.uio.no",
	description="Instagram filters in Python",
	url="https://github.uio.no/IN3110/IN3110-adalw/",
	packages=setuptools.find_packages(),
	scripts=['instapy/bin/insta']
	)