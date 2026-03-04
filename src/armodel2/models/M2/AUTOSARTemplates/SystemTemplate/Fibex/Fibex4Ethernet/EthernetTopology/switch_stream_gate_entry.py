"""SwitchStreamGateEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 142)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwitchStreamGateEntry(Identifiable):
    """AUTOSAR SwitchStreamGateEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SWITCH-STREAM-GATE-ENTRY"


    internal_priority: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "INTERNAL-PRIORITY": lambda obj, elem: setattr(obj, "internal_priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize SwitchStreamGateEntry."""
        super().__init__()
        self.internal_priority: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SwitchStreamGateEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwitchStreamGateEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize internal_priority
        if self.internal_priority is not None:
            serialized = SerializationHelper.serialize_item(self.internal_priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERNAL-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamGateEntry":
        """Deserialize XML element to SwitchStreamGateEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchStreamGateEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchStreamGateEntry, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INTERNAL-PRIORITY":
                setattr(obj, "internal_priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class SwitchStreamGateEntryBuilder(IdentifiableBuilder):
    """Builder for SwitchStreamGateEntry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwitchStreamGateEntry = SwitchStreamGateEntry()


    def with_internal_priority(self, value: Optional[PositiveInteger]) -> "SwitchStreamGateEntryBuilder":
        """Set internal_priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.internal_priority = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "internalPriority",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwitchStreamGateEntry:
        """Build and return the SwitchStreamGateEntry instance with validation."""
        self._validate_instance()
        return self._obj