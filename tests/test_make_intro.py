from tools.make_audiobook import DEFAULT_VOICE, VOICES
from tools.make_intro import dest_name


def test_intro_dest_name_default_voice():
    # the default voice (Ryan) keeps the bare, historical name
    assert dest_name(DEFAULT_VOICE) == "intro.mp3"
    assert dest_name("ryan") == "intro.mp3"


def test_intro_dest_name_other_voices():
    for key in ("sonia", "andrew", "ava", "william", "natasha", "connor", "emily"):
        assert dest_name(key) == f"{key}-intro.mp3"


def test_intro_dest_name_covers_all_eight_voices():
    names = {dest_name(k) for k in VOICES}
    assert len(names) == len(VOICES) == 8
    assert names == {"intro.mp3"} | {
        f"{k}-intro.mp3" for k in VOICES if k != DEFAULT_VOICE
    }
