import pytest, src.masks as masks

error_message = 'Указан некорректный номер карты, повторите попытку'
@pytest.mark.parametrize('value, expected',[('',error_message),
                                            ('1234567891234567', '1234 56 ** ** ** 4567'),
                                            ('12323455',error_message)])


@pytest.fixture
def test_mask():
    return 'Указан некорректный номер счета, повторите попытку'

