
valid_fields = [
    # geoip
    "country_code",
    "country_code3",
    "country_name",
    "region",
    "city",
    "postal_code",
    "latitude",
    "longitude",
    "region_name",
    "time_zone",
    "dma_code",
    "metro_code",
    "area_code",

    # rdap
    "nir",
    "asn_registry", 
    "asn",
    "asn_cidr",
    "asn_country_code",
    "asn_date",
    "asn_description",
]


def parse_filter(syntax):
    filters = {}

    for i in syntax.split(','):
        terms = i.split('=')
        if len(terms) != 2:
            continue
        
        field, value = terms
        field = field.lower()
        if field not in valid_fields:
            return "Filter error: {} is not a valid field.".format(field)

        filters[field] = value
    
    if filters:
        return filters
    return None


def parse_data(data, filters):
    for f in filters:
        if not (f in data and filters[f] == data[f]):
            break
    else:
        return data

    return None