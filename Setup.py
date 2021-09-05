from setuptools import setup

with open('README.md','r') as file:
    long_description=file.read()

setup(
   name='NanDealer',
   version='1.0',
   description='A library which can deal with Nan values in a dataframe',
   license="MIT",
   long_description=long_description,
   author='Atul Rai',
   author_email='iamatul1214@gmail.com',
   url="",
   packages=['NanDealer'],  #same as name
   install_requires=['pandas'], #external packages as dependencies
   classifiers=[
       "programming language :: Python :: 3.6 and above"],

)