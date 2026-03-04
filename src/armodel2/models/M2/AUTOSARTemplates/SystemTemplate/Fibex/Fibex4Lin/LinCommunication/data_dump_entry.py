"""DataDumpEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 439)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import LinConfigurationEntryBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataDumpEntry(LinConfigurationEntry):
    """AUTOSAR DataDumpEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-DUMP-ENTRY"


    byte_values: list[Integer]
    _DESERIALIZE_DISPATCH = {
        "BYTE-VALUES": lambda obj, elem: obj.byte_values.append(SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize DataDumpEntry."""
        super().__init__()
        self.byte_values: list[Integer] = []

    def serialize(self) -> ET.Element:
        """Serialize DataDumpEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataDumpEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize byte_values (list to container "BYTE-VALUES")
        if self.byte_values:
            wrapper = ET.Element("BYTE-VALUES")
            for item in self.byte_values:
                serialized = SerializationHelper.serialize_item(item, "Integer")
                if serialized is not None:
                    child_elem = ET.Element("BYTE-VALUE")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataDumpEntry":
        """Deserialize XML element to DataDumpEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataDumpEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataDumpEntry, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BYTE-VALUES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.byte_values.append(SerializationHelper.deserialize_by_tag(item_elem, "Integer"))

        return obj



class DataDumpEntryBuilder(LinConfigurationEntryBuilder):
    """Builder for DataDumpEntry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataDumpEntry = DataDumpEntry()


    def with_byte_values(self, items: list[Integer]) -> "DataDumpEntryBuilder":
        """Set byte_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.byte_values = list(items) if items else []
        return self


    def add_byte_value(self, item: Integer) -> "DataDumpEntryBuilder":
        """Add a single item to byte_values list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.byte_values.append(item)
        return self

    def clear_byte_values(self) -> "DataDumpEntryBuilder":
        """Clear all items from byte_values list.

        Returns:
            self for method chaining
        """
        self._obj.byte_values = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "byteValue",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DataDumpEntry:
        """Build and return the DataDumpEntry instance with validation."""
        self._validate_instance()
        return self._obj