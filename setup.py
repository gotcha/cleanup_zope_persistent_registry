from setuptools import setup, find_packages

version = '0.1'

long_description = (
    open('README.txt').read()
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
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
