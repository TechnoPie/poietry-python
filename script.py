[tool.poetry]
name = "my-python-project"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"
packages = [{include = "my_python_project"}]

[tool.poetry.dependencies]
python = "^3.8" # Or whatever Python version Poetry detected/you specified
numpy = [
    { version = "1.17.3", markers = "python_version < '3.9'" },
    { version = "1.21.1", markers = "python_version >= '3.9'" },
]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
