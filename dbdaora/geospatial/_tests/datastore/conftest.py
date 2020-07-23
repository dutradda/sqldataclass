import pytest

from dbdaora import DatastoreDataSource, DatastoreGeoSpatialRepository


@pytest.fixture
def fallback_data_source():
    return DatastoreDataSource()


@pytest.fixture
def fake_repository_cls(fake_entity_cls):
    class FakeGeoSpatialRepository(DatastoreGeoSpatialRepository):
        name = 'fake'
        key_attrs = ('fake2_id', 'fake_id')
        entity_cls = fake_entity_cls

    return FakeGeoSpatialRepository
