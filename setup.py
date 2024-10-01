from setuptools import setup, find_packages # type: ignore

setup(
    name="recon-tool",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "dnspython",
        "python-whois",
    ],
    entry_points={
        "console_scripts": [
            "recon-tool=recon_tool.main:main",
        ],
    },
)
