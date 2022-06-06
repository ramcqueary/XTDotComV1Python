from setuptools import setup


setup(
  name='xtdotcomv1',
  version='1.0.0',
  author='Richard McQueary',
  packages=['xtdotcomv1',
              'xtdotcomv1.utils',
              'xtdotcomv1.public'],
  install_requires=['requests','pandas'],
  zip_safe=False
)
