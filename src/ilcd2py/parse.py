

def parse_process_information(ilcd_data: dict[str, dict]) -> dict:
    return {"process": True}


def parse_modelling_and_validation(ilcd_data: dict[str, dict]) -> dict:
    return {"modelling": True}


def parse_administrative_information(ilcd_data: dict[str, dict]) -> dict:
    return {"admin": True}


def parse_exchanges(ilcd_data: dict[str, dict]) -> dict:
    return {"exchanges": True}


def parse_lcia_results(ilcd_data: dict[str, dict]) -> dict:

    return {"lcia": True}


def parse_ilcd(ilcd_data: dict[str, dict]) -> dict:
    epd = {}
    epd.update(parse_process_information(ilcd_data))
    epd.update(parse_modelling_and_validation(ilcd_data))
    epd.update(parse_administrative_information(ilcd_data))
    epd.update(parse_exchanges(ilcd_data))
    epd.update(parse_lcia_results(ilcd_data))

    return epd
