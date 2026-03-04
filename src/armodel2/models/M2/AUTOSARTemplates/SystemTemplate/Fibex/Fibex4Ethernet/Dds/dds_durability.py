"""DdsDurability AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 530)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsDurabilityKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsDurability(ARObject):
    """AUTOSAR DdsDurability."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-DURABILITY"


    durability_kind: Optional[DdsDurabilityKindEnum]
    _DESERIALIZE_DISPATCH = {
        "DURABILITY-KIND": lambda obj, elem: setattr(obj, "durability_kind", DdsDurabilityKindEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DdsDurability."""
        super().__init__()
        self.durability_kind: Optional[DdsDurabilityKindEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsDurability to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsDurability, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize durability_kind
        if self.durability_kind is not None:
            serialized = SerializationHelper.serialize_item(self.durability_kind, "DdsDurabilityKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DURABILITY-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsDurability":
        """Deserialize XML element to DdsDurability object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsDurability object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsDurability, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DURABILITY-KIND":
                setattr(obj, "durability_kind", DdsDurabilityKindEnum.deserialize(child))

        return obj



class DdsDurabilityBuilder(BuilderBase):
    """Builder for DdsDurability with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsDurability = DdsDurability()


    def with_durability_kind(self, value: Optional[DdsDurabilityKindEnum]) -> "DdsDurabilityBuilder":
        """Set durability_kind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.durability_kind = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "durabilityKind",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DdsDurability:
        """Build and return the DdsDurability instance with validation."""
        self._validate_instance()
        return self._obj