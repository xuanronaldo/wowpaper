from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='wowpaper',
    version='1.0.0',
    description='A wallpaper application programed by Python, it could run on any desktop OS.',
    long_description=readme,
    author='Xuan Ronaldo',
    author_email='xuanronaldo@outlook.com',
    url='https://github.com/xuanronaldo/wowpaper',
    license=license,
    packages=find_packages()
)
