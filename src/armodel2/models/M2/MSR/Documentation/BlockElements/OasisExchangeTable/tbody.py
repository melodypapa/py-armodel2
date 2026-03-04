"""Tbody AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 335)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    ValignEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Tbody(ARObject):
    """AUTOSAR Tbody."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TBODY"


    valign: Optional[ValignEnum]
    _DESERIALIZE_DISPATCH = {
        "VALIGN": lambda obj, elem: setattr(obj, "valign", ValignEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize Tbody."""
        super().__init__()
        self.valign: Optional[ValignEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize Tbody to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Tbody, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize valign
        if self.valign is not None:
            serialized = SerializationHelper.serialize_item(self.valign, "ValignEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALIGN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Tbody":
        """Deserialize XML element to Tbody object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Tbody object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Tbody, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "VALIGN":
                setattr(obj, "valign", ValignEnum.deserialize(child))

        return obj



class TbodyBuilder(BuilderBase):
    """Builder for Tbody with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Tbody = Tbody()


    def with_valign(self, value: Optional[ValignEnum]) -> "TbodyBuilder":
        """Set valign attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.valign = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "valign",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Tbody:
        """Build and return the Tbody instance with validation."""
        self._validate_instance()
        return self._obj