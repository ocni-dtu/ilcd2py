from ilcd2py.parse import parse_ilcd


def test_parse_process_information(ilcd_data):
    pass


def test_parse_modelling_and_validation(ilcd_data):
    pass


def test_parse_administrative_information(ilcd_data):
    pass


def test_parse_exchanges(ilcd_data):
    pass


def test_parse_lcia_results(ilcd_data):
    pass


def test_parse_ilcd(ilcd_data):
    epd = parse_ilcd(ilcd_data)

    assert epd
    assert len(epd.keys())
