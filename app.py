# -*- coding: utf-8 -*-

import fire


def app(
    name: str = "World",
):
    """
    This is App 1.
    """
    print(f"Hello, {name}!")


if __name__ == "__main__":
    fire.Fire(app)
