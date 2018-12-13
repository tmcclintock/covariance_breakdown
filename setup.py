from setuptools import setup

dist = setup(name="covariance_breakdown",
             author="Thomas McClintock",
             author_email="mcclintock@bnl.gov",
             description="Tool for breaking down covariance matrices.",
             license="MIT",
             url="https://github.com/tmcclintock/covariance_breakdown",
             packages=['breakdown'],
             long_description=open("README.md").read()
)
