from gittip.testing import tip_graph
from gittip.elsewhere import github, twitter, devnet


def test_github_resolve_resolves():
    with tip_graph(('alice', 'bob', 1)):
        expected = 'alice'
        actual = github.resolve(u'alice')
        assert actual == expected, actual

def test_devnet_resolve_resolves():
    with tip_graph(('alice', 'bob', 1, True, False, False, "devnet", "7890")):
        expected = 'alice'
        actual = devnet.resolve(u'alice')
        assert actual == expected, actual

def test_twitter_resolve_resolves():
    with tip_graph(('alice', 'bob', 1, True, False, False, "twitter", "2345")):
        expected = 'alice'
        actual = twitter.resolve(u'alice')
        assert actual == expected, actual
