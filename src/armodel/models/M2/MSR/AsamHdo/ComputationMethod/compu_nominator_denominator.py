"""CompuNominatorDenominator AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 391)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class CompuNominatorDenominator(ARObject):
    """AUTOSAR CompuNominatorDenominator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    v: list[Numerical]
    def __init__(self) -> None:
        """Initialize CompuNominatorDenominator."""
        super().__init__()
        self.v: list[Numerical] = []

    def serialize(self) -> ET.Element:
        """Serialize CompuNominatorDenominator to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Serialize v (list)
        for item in self.v:
            serialized = SerializationHelper.serialize_item(item, "Numerical")
            if serialized is not None:
                # For non-container lists, wrap with correct tag
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

        # Parse v (list)
        obj.v = []
        for child in SerializationHelper.find_all_child_elements(element, "V"):
            v_value = child.text
            obj.v.append(v_value)

        return obj



class CompuNominatorDenominatorBuilder:
    """Builder for CompuNominatorDenominator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuNominatorDenominator = CompuNominatorDenominator()

    def build(self) -> CompuNominatorDenominator:
        """Build and return CompuNominatorDenominator object.

        Returns:
            CompuNominatorDenominator instance
        """
        # TODO: Add validation
        return self._obj
