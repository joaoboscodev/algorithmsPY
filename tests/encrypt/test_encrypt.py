from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(111, 2)

    with pytest.raises(TypeError):
        encrypt_message("Joaobosco", "naoKey")

    assert encrypt_message("Chagas", 3) == "ahC_sag"

    assert encrypt_message("Joao", 2) == "oa_oJ"

    assert encrypt_message("Bosco", 4) == "o_csoB"

    assert encrypt_message("Joao", 4) == "oaoJ"
