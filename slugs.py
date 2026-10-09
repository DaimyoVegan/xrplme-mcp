"""GENERATED from the local Phase 3A artifact. Closed enum of the 30 exact slugs.

No normalization, no aliases, no fuzzy matching: a slug is valid only if it
appears verbatim in SLUGS.
"""
from .errors import UnknownCountrySlug

SLUGS = (
    "australia",
    "brazil",
    "brunei",
    "canada",
    "france",
    "germany",
    "hong_kong",
    "india",
    "indonesia",
    "italy",
    "japan",
    "korea",
    "laos",
    "macau",
    "malaysia",
    "mexico",
    "myanmar",
    "netherlands",
    "newzealand",
    "papua-new-guinea",
    "philippines",
    "singapore",
    "switzerland",
    "taiwan",
    "thailand",
    "timor-leste",
    "uae",
    "uk",
    "usa",
    "vietnam",
)

_SLUG_SET = frozenset(SLUGS)

EXPECTED_RECORDS = {
    "australia": 24,
    "brazil": 22,
    "brunei": 23,
    "canada": 20,
    "france": 23,
    "germany": 24,
    "hong_kong": 50,
    "india": 35,
    "indonesia": 26,
    "italy": 17,
    "japan": 20,
    "korea": 20,
    "laos": 20,
    "macau": 25,
    "malaysia": 28,
    "mexico": 20,
    "myanmar": 19,
    "netherlands": 60,
    "newzealand": 26,
    "papua-new-guinea": 23,
    "philippines": 27,
    "singapore": 47,
    "switzerland": 23,
    "taiwan": 11,
    "thailand": 25,
    "timor-leste": 23,
    "uae": 28,
    "uk": 62,
    "usa": 47,
    "vietnam": 24,
}

DISPLAY_NAMES = {
    "australia": "Australia",
    "brazil": "Brazil",
    "brunei": "Brunei",
    "canada": "Canada",
    "france": "France",
    "germany": "Germany",
    "hong_kong": "Hong Kong",
    "india": "India",
    "indonesia": "Indonesia",
    "italy": "Italy",
    "japan": "Japan",
    "korea": "South Korea",
    "laos": "Laos",
    "macau": "Macau",
    "malaysia": "Malaysia",
    "mexico": "Mexico",
    "myanmar": "Myanmar",
    "netherlands": "Netherlands",
    "newzealand": "New Zealand",
    "papua-new-guinea": "Papua New Guinea",
    "philippines": "Philippines",
    "singapore": "Singapore",
    "switzerland": "Switzerland",
    "taiwan": "Taiwan",
    "thailand": "Thailand",
    "timor-leste": "Timor-Leste",
    "uae": "United Arab Emirates",
    "uk": "United Kingdom",
    "usa": "United States",
    "vietnam": "Vietnam",
}

SOURCE_UPDATED_AT = {
    "australia": "2026-09-08T01:09:05.464088+00:00",
    "brazil": "2026-09-08T09:49:39.153341+00:00",
    "brunei": "2026-09-20T22:00:10.245127+00:00",
    "canada": "2026-09-07T22:52:17.332310+00:00",
    "france": "2026-09-08T09:36:25.812389+00:00",
    "germany": "2026-09-08T01:12:23.409041+00:00",
    "hong_kong": "2026-09-08T20:26:08.379736+00:00",
    "india": "2026-09-07T19:42:07.531454+00:00",
    "indonesia": "2026-09-19T20:09:20.901682+00:00",
    "italy": "2026-09-21T04:54:10.464782+00:00",
    "japan": "2026-09-07T12:44:17.621131+00:00",
    "korea": "2026-09-07T16:07:21.342686+00:00",
    "laos": "2026-09-20T22:00:22.527193+00:00",
    "macau": "2026-09-19T20:10:00.135284+00:00",
    "malaysia": "2026-09-19T20:08:59.812732+00:00",
    "mexico": "2026-09-08T10:38:44.475796+00:00",
    "myanmar": "2026-09-20T22:00:34.815609+00:00",
    "netherlands": "2026-09-08T10:44:45.271730+00:00",
    "newzealand": "2026-09-19T20:10:20.427460+00:00",
    "papua-new-guinea": "2026-09-20T22:01:20.343140+00:00",
    "philippines": "2026-09-08T01:01:44.699369+00:00",
    "singapore": "2026-09-08T01:05:17.420787+00:00",
    "switzerland": "2026-09-08T10:40:37.838940+00:00",
    "taiwan": "2026-09-19T20:09:40.492589+00:00",
    "thailand": "2026-09-08T01:42:00.220742+00:00",
    "timor-leste": "2026-09-20T22:01:04.496040+00:00",
    "uae": "2026-09-08T00:02:03.122463+00:00",
    "uk": "2026-09-08T00:10:38.042603+00:00",
    "usa": "2026-09-07T21:26:59.826175+00:00",
    "vietnam": "2026-09-07T11:46:12.950689+00:00",
}


def validate_slug(slug):
    """Exact-match validation against the closed enum. Raises before any I/O."""
    if not isinstance(slug, str) or slug not in _SLUG_SET:
        raise UnknownCountrySlug(
            "unknown country slug %r: must be one of the 30 exact slugs" % (slug,)
        )
    return slug
