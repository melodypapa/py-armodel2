"""DdsOwnershipStrength AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 533)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsOwnershipStrength(ARObject):
    """AUTOSAR DdsOwnershipStrength."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-OWNERSHIP-STRENGTH"


    ownership: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "OWNERSHIP": lambda obj, elem: setattr(obj, "ownership", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DdsOwnershipStrength."""
        super().__init__()
        self.ownership: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsOwnershipStrength to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsOwnershipStrength, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ownership
        if self.ownership is not None:
            serialized = SerializationHelper.serialize_item(self.ownership, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OWNERSHIP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsOwnershipStrength":
        """Deserialize XML element to DdsOwnershipStrength object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsOwnershipStrength object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsOwnershipStrength, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OWNERSHIP":
                setattr(obj, "ownership", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DdsOwnershipStrengthBuilder(BuilderBase):
    """Builder for DdsOwnershipStrength with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsOwnershipStrength = DdsOwnershipStrength()


    def with_ownership(self, value: Optional[PositiveInteger]) -> "DdsOwnershipStrengthBuilder":
        """Set ownership attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ownership = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ownership",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DdsOwnershipStrength:
        """Build and return the DdsOwnershipStrength instance with validation."""
        self._validate_instance()
        return self._obj