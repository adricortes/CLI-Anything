from setuptools import setup, find_namespace_packages

setup(
    name="cli-anything-wiremock",
    version="0.1.0",
    description="CLI harness for WireMock HTTP mock server administration",
    long_description=open("WIREMOCK.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_namespace_packages(include=["cli_anything.*"]),
    include_package_data=True,
    package_data={"cli_anything.wiremock": ["skills/*.md", "*.md"]},
    install_requires=["click>=8.0", "requests>=2.28", "rich>=13.0"],
    entry_points={
        "console_scripts": [
            "cli-anything-wiremock=cli_anything.wiremock.wiremock_cli:cli"
        ]
    },
    python_requires=">=3.10",
)
