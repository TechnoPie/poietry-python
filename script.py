[tool.poetry]
name = "my-python-project"
version = "0.1.0"

[tool.poetry.dependencies]
python = "^3.8"
numpy = [
    { version = "1.17.3", markers = "python_version < '3.9'" },
    { version = "1.21.1", markers = "python_version >= '3.9'" },
]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
