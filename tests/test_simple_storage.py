import pytest
from brownie import SimpleStorage, accounts


@pytest.fixture
def simple_storage():
    # Arrange / Act
    simple_storage = SimpleStorage.deploy(
        {"from": accounts[0]},
    )
    simple_storage.tx.wait(1)
    # Assert
    assert simple_storage is not None
    return simple_storage

def test_setNumber(simple_storage):
    assert simple_storage.number() == 0
    simple_storage.setNumber(777)
    assert simple_storage.number() == 777
