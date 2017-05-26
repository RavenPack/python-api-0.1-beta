from ravenpackapi.core import RPApi


def test_inline_entity_mapping():
    entities = [{'ticker': 'AAPL'},
                {'ticker': 'JPM'},
                {'listing': 'XNYS:DVN'}]
    api = RPApi()
    mapping = api.get_entity_mapping(entities)
    assert not mapping.get('errors')
    assert mapping['IDENTIFIERS_MATCHED_COUNT'] == mapping['IDENTIFIERS_SUBMITTED_COUNT'] == 3

    # let's get the first mapped entities
    rp_entities_id = [e['RP_ENTITIES'][0]['RP_ENTITY_ID'] for e in mapping['IDENTIFIERS_MAPPED']]
    assert rp_entities_id == ['D8442A', '619882', '14BA06']
