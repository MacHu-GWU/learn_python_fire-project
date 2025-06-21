# -*- coding: utf-8 -*-

from learn_python_fire import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_python_fire.tests import run_cov_test

    run_cov_test(
        __file__,
        "learn_python_fire.api",
        preview=False,
    )
