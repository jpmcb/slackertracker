import click
from flask import Flask

from slackertracker.app import create_app

app, db = create_app('instance/config.json')

@app.cli.command()
def test():
    import unittest
    from slackertracker.tests.suite import suite
    unittest.TextTestRunner().run(suite)