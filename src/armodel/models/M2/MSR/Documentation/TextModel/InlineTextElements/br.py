"""Br AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 316)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class Br(ARObject):
    """AUTOSAR Br."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize Br."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize Br to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Br, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "Br":
        """Deserialize XML element to Br object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Br object
        """
        # Delegate to parent class to handle inherited attributes
        return super(Br, cls).deserialize(element)



class BrBuilder:
    """Builder for Br."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Br = Br()

    def build(self) -> Br:
        """Build and return Br object.

        Returns:
            Br instance
        """
        # TODO: Add validation
        return self._obj
