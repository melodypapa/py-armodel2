"""NumericalValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 302)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 241)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class NumericalValueVariationPoint(ARObject):
    """AUTOSAR NumericalValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize NumericalValueVariationPoint."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize NumericalValueVariationPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NumericalValueVariationPoint, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "NumericalValueVariationPoint":
        """Deserialize XML element to NumericalValueVariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NumericalValueVariationPoint object
        """
        # Delegate to parent class to handle inherited attributes
        return super(NumericalValueVariationPoint, cls).deserialize(element)



class NumericalValueVariationPointBuilder:
    """Builder for NumericalValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NumericalValueVariationPoint = NumericalValueVariationPoint()

    def build(self) -> NumericalValueVariationPoint:
        """Build and return NumericalValueVariationPoint object.

        Returns:
            NumericalValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
