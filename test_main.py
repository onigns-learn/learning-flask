from . import create_app

def test_shorten(client):
    resp = client.get('/')
    assert b'Shortener' in resp.data