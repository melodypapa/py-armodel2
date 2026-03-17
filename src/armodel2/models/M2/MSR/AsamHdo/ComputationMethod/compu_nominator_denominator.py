"""CompuNominatorDenominator AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 391)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, ClassVar, Dict
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import xml_element_name

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CompuNominatorDenominator(ARObject):
    """AUTOSAR CompuNominatorDenominator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COMPU-NOMINATOR-DENOMINATOR"


    # Pre-computed attribute name → XML tag mappings (exceptional cases only)
    # Normal attributes use NameConverter.to_xml_tag() for calculation
    _ATTRIBUTE_XML_TAG_MAPPING: ClassVar[Dict[str, str]] = {
        "vs": "V",
    }

    _vs: list[Numerical]
    _DESERIALIZE_DISPATCH = {
        "V": lambda obj, elem: obj._vs.append(SerializationHelper.deserialize_by_tag(elem, "Numerical")),
    }


    def __init__(self) -> None:
        """Initialize CompuNominatorDenominator."""
        super().__init__()
        self._vs: list[Numerical] = []
    @property
    @xml_element_name("V")
    def vs(self) -> list[Numerical]:
        """Get vs with custom XML element name."""
        return self._vs

    @vs.setter
    def vs(self, value: list[Numerical]) -> None:
        """Set vs with custom XML element name."""
        self._vs = value


    def serialize(self) -> ET.Element:
        """Serialize CompuNominatorDenominator to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompuNominatorDenominator, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize vs (list of direct "V" children, no container)
        if self.vs:
            for item in self.vs:
                serialized = SerializationHelper.serialize_item(item, "Numerical")
                if serialized is not None:
                    # Wrap with correct tag from @xml_element_name decorator
                    wrapped = ET.Element("V")
                    if hasattr(serialized, 'attrib'):
                        wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                    for child in serialized:
                        wrapped.append(child)
                    elem.append(wrapped)
        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuNominatorDenominator":
        """Deserialize XML element to CompuNominatorDenominator object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuNominatorDenominator object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompuNominatorDenominator, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "V":
                obj._vs.append(SerializationHelper.deserialize_by_tag(child, "Numerical"))

        return obj



class CompuNominatorDenominatorBuilder(BuilderBase):
    """Builder for CompuNominatorDenominator with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CompuNominatorDenominator = CompuNominatorDenominator()


    def with_vs(self, items: list[Numerical]) -> "CompuNominatorDenominatorBuilder":
        """Set vs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.vs = list(items) if items else []
        return self


    def add_v(self, item: Numerical) -> "CompuNominatorDenominatorBuilder":
        """Add a single item to vs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.vs.append(item)
        return self

    def clear_vs(self) -> "CompuNominatorDenominatorBuilder":
        """Clear all items from vs list.

        Returns:
            self for method chaining
        """
        self._obj.vs = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "v",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CompuNominatorDenominator:
        """Build and return the CompuNominatorDenominator instance with validation."""
        self._validate_instance()
        return self._obj