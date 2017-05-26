from ravenpackapi.core import RPApi
from ravenpackapi.tests.known_facts import GOOGLE_RP_ENTITY_ID, APPLE_RP_ENTITY_ID


def test_inline_entity_reference():
    entities = [GOOGLE_RP_ENTITY_ID, APPLE_RP_ENTITY_ID]
    api = RPApi()
    reference = api.get_entity_reference(entities)
    assert not reference.get('errors')
    assert len(reference['reference_data']) == 2, 'Expecting two reference results'
    google, apple = reference['reference_data']

    assert GOOGLE_RP_ENTITY_ID in google
    assert google[GOOGLE_RP_ENTITY_ID]['ENTITY_NAME'][-1]['DATA_VALUE'] == 'Alphabet Inc.'

    assert APPLE_RP_ENTITY_ID in apple
    assert apple[APPLE_RP_ENTITY_ID]['ENTITY_NAME'][-1]['DATA_VALUE'] == 'Apple Inc.'
