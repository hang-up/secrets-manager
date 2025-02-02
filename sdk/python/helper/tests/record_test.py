import unittest
from keeper_secrets_manager_helper.record import Record
from keeper_secrets_manager_core.dto.dtos import RecordCreate


class RecordTest(unittest.TestCase):

    def test_build_record_simple(self):

        """Test the ingress in the helper create record

        Instead of calling the version modules directory, this will call them. Basically one entry
        point for all versions.

        """

        contact_data = [
            "f.name.first=John",
            "f.name.last=Smith",
            "f.text=ACME",
            "f.email=admin@localhost",
            'f.phone={"number": "5552223333", "type": "Work"}',
            'f.phone={"number": "5551111111", "type": "Home"}',
            'f.addressRef=PpR0AKIZAtUiyvq1r2BC1w',
            'c.password='
        ]

        kwargs = dict(
            record_type='contact',
            title="Contact Record",
            notes="My Note",
            field_args=contact_data,
            password_generate=True
        )

        r = Record(version="v3").create_from_field_args(**kwargs)
        record_create_obj = r[0].get_record_create_obj()
        self.assertIsInstance(record_create_obj, RecordCreate)
        self.assertEqual("Contact Record", record_create_obj.title)
        self.assertEqual("My Note", record_create_obj.notes)
        self.assertListEqual(record_create_obj.fields[0].value, [{'first': 'John', 'last': 'Smith'}])
        self.assertListEqual(record_create_obj.fields[1].value, ["ACME"])
        self.assertListEqual(record_create_obj.fields[2].value, ["admin@localhost"])
        self.assertListEqual(record_create_obj.fields[3].value, [{"number": "5552223333", "type": "Work"},
                             {"number": "5551111111", "type": "Home"}])
        self.assertListEqual(record_create_obj.fields[4].value, ["PpR0AKIZAtUiyvq1r2BC1w"])
        self.assertNotEqual(0, len(record_create_obj.custom[0].value))
