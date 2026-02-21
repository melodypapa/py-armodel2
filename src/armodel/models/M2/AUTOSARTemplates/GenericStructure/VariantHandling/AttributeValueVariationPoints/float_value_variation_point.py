"""FloatValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 240)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class FloatValueVariationPoint(ARObject):
    """AUTOSAR FloatValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize FloatValueVariationPoint."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize FloatValueVariationPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FloatValueVariationPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FloatValueVariationPoint":
        """Deserialize XML element to FloatValueVariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FloatValueVariationPoint object
        """
        # Delegate to parent class to handle inherited attributes
        return super(FloatValueVariationPoint, cls).deserialize(element)



class FloatValueVariationPointBuilder:
    """Builder for FloatValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FloatValueVariationPoint = FloatValueVariationPoint()

    def build(self) -> FloatValueVariationPoint:
        """Build and return FloatValueVariationPoint object.

        Returns:
            FloatValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
