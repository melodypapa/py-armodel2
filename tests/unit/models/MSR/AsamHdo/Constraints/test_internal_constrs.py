"""Unit tests for InternalConstrs serialization with Limit types."""

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.internal_constrs import InternalConstrs
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.limit import Limit
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.interval_type_enum import IntervalTypeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.monotony_enum import MonotonyEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.numerical import Numerical


class TestInternalConstrsSerialization:
    """Unit tests for InternalConstrs serialization with Limit types."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.internal_constrs = InternalConstrs()

    def test_serialize_internal_constrs_with_limits(self):
        """Test InternalConstrs serialization with lower_limit and upper_limit."""
        self.internal_constrs.lower_limit = Limit(value="-32768", interval_type=IntervalTypeEnum.CLOSED)
        self.internal_constrs.upper_limit = Limit(value="32767", interval_type=IntervalTypeEnum.CLOSED)

        elem = self.internal_constrs.serialize()

        # Verify limits are wrapped with correct tag names
        lower_limit_elem = elem.find("LOWER-LIMIT")
        assert lower_limit_elem is not None
        assert lower_limit_elem.text == "-32768"
        assert lower_limit_elem.get("INTERVAL-TYPE") == "CLOSED"

        upper_limit_elem = elem.find("UPPER-LIMIT")
        assert upper_limit_elem is not None
        assert upper_limit_elem.text == "32767"
        assert upper_limit_elem.get("INTERVAL-TYPE") == "CLOSED"

    def test_serialize_internal_constrs_with_open_interval_type(self):
        """Test InternalConstrs serialization with OPEN interval type."""
        self.internal_constrs.lower_limit = Limit(value="0", interval_type=IntervalTypeEnum.OPEN)
        self.internal_constrs.upper_limit = Limit(value="100", interval_type=IntervalTypeEnum.OPEN)

        elem = self.internal_constrs.serialize()

        lower_limit_elem = elem.find("LOWER-LIMIT")
        assert lower_limit_elem.get("INTERVAL-TYPE") == "OPEN"

        upper_limit_elem = elem.find("UPPER-LIMIT")
        assert upper_limit_elem.get("INTERVAL-TYPE") == "OPEN"

    def test_serialize_internal_constrs_without_interval_type(self):
        """Test InternalConstrs serialization without interval_type (optional attribute)."""
        self.internal_constrs.lower_limit = Limit(value="0")
        self.internal_constrs.upper_limit = Limit(value="100")

        elem = self.internal_constrs.serialize()

        lower_limit_elem = elem.find("LOWER-LIMIT")
        assert lower_limit_elem is not None
        assert lower_limit_elem.text == "0"
        assert lower_limit_elem.get("INTERVAL-TYPE") is None

    def test_serialize_internal_constrs_with_monotony(self):
        """Test InternalConstrs serialization with monotony enum."""
        self.internal_constrs.monotony = MonotonyEnum.STRICTLY_INCREASING

        elem = self.internal_constrs.serialize()

        monotony_elem = elem.find("MONOTONY")
        assert monotony_elem is not None
        # Verify enum value is serialized as uppercase
        assert monotony_elem.text == "STRICTLYINCREASING"

    def test_deserialize_internal_constrs_with_limits(self):
        """Test InternalConstrs deserialization with Limit types."""
        xml = '''<INTERNAL-CONSTRS>
            <LOWER-LIMIT INTERVAL-TYPE="CLOSED">-32768</LOWER-LIMIT>
            <UPPER-LIMIT INTERVAL-TYPE="OPEN">32767</UPPER-LIMIT>
        </INTERNAL-CONSTRS>'''

        elem = ET.fromstring(xml)
        obj = InternalConstrs.deserialize(elem)

        # Verify limits are deserialized correctly
        assert obj.lower_limit is not None
        assert obj.lower_limit.value == "-32768"
        assert obj.lower_limit.interval_type == IntervalTypeEnum.CLOSED

        assert obj.upper_limit is not None
        assert obj.upper_limit.value == "32767"
        assert obj.upper_limit.interval_type == IntervalTypeEnum.OPEN

    def test_deserialize_internal_constrs_with_monotony_lowercase(self):
        """Test InternalConstrs deserialization with lowercase monotony value."""
        xml = '''<INTERNAL-CONSTRS>
            <MONOTONY>strictlyincreasing</MONOTONY>
        </INTERNAL-CONSTRS>'''

        elem = ET.fromstring(xml)
        obj = InternalConstrs.deserialize(elem)

        # Verify enum is deserialized case-insensitively
        assert obj.monotony == MonotonyEnum.STRICTLY_INCREASING

    def test_deserialize_internal_constrs_with_monotony_uppercase(self):
        """Test InternalConstrs deserialization with uppercase monotony value."""
        xml = '''<INTERNAL-CONSTRS>
            <MONOTONY>STRICTLYINCREASING</MONOTONY>
        </INTERNAL-CONSTRS>'''

        elem = ET.fromstring(xml)
        obj = InternalConstrs.deserialize(elem)

        assert obj.monotony == MonotonyEnum.STRICTLY_INCREASING

    def test_round_trip_internal_constrs_with_limits(self):
        """Test InternalConstrs round-trip serialization with Limit types."""
        # Setup
        self.internal_constrs.lower_limit = Limit(value="0", interval_type=IntervalTypeEnum.CLOSED)
        self.internal_constrs.upper_limit = Limit(value="100", interval_type=IntervalTypeEnum.CLOSED)
        self.internal_constrs.monotony = MonotonyEnum.MONOTONOUS

        # Serialize
        elem = self.internal_constrs.serialize()

        # Deserialize
        reloaded = InternalConstrs.deserialize(elem)

        # Verify all attributes are preserved
        assert reloaded.lower_limit is not None
        assert reloaded.lower_limit.value == "0"
        assert reloaded.lower_limit.interval_type == IntervalTypeEnum.CLOSED

        assert reloaded.upper_limit is not None
        assert reloaded.upper_limit.value == "100"
        assert reloaded.upper_limit.interval_type == IntervalTypeEnum.CLOSED

        assert reloaded.monotony == MonotonyEnum.MONOTONOUS

    def test_round_trip_internal_constrs_with_all_attributes(self):
        """Test InternalConstrs round-trip with all possible attributes."""
        # Setup
        self.internal_constrs.lower_limit = Limit(value="-128", interval_type=IntervalTypeEnum.CLOSED)
        self.internal_constrs.upper_limit = Limit(value="127", interval_type=IntervalTypeEnum.CLOSED)
        self.internal_constrs.monotony = MonotonyEnum.MONOTONOUS
        self.internal_constrs.max_diff = Numerical(10)
        self.internal_constrs.max_gradient = Numerical(5)

        # Serialize
        elem = self.internal_constrs.serialize()

        # Deserialize
        reloaded = InternalConstrs.deserialize(elem)

        # Verify all attributes
        assert reloaded.lower_limit is not None
        assert reloaded.lower_limit.value == "-128"
        assert reloaded.lower_limit.interval_type == IntervalTypeEnum.CLOSED

        assert reloaded.upper_limit is not None
        assert reloaded.upper_limit.value == "127"
        assert reloaded.upper_limit.interval_type == IntervalTypeEnum.CLOSED

        assert reloaded.monotony == MonotonyEnum.MONOTONOUS
        assert reloaded.max_diff is not None
        assert reloaded.max_gradient is not None