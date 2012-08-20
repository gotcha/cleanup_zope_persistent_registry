from setuptools import setup, find_packages

version = '0.2dev'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='cleanup_zope_persistent_registry',
      version=version,
      description="Cleanup of keys leftover in zope component registries",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Godefroid Chapelle',
      author_email='gotcha@bubblenet.be',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      extras_require=dict(
          test=[
          'unittest2',
          'zope.component',
          'zope.interface',
          'ZODB3',
          ],
      ),
      )
