from setuptools import setup, find_packages

print find_packages()

setup(
    name='django-value-ladder',
    version='0.1',
    description='Things value definition application.',
    author='Vaclav Klecanda',
    author_email='vencax77@gmail.com',
    url='vxk.cz',
    packages=find_packages(),
    include_package_data=True,
)
