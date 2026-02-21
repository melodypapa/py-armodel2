"""SecurityEventContextData AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 66)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SecurityEventContextData(ARObject):
    """AUTOSAR SecurityEventContextData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SecurityEventContextData."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventContextData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventContextData, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextData":
        """Deserialize XML element to SecurityEventContextData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventContextData object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SecurityEventContextData, cls).deserialize(element)



class SecurityEventContextDataBuilder:
    """Builder for SecurityEventContextData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextData = SecurityEventContextData()

    def build(self) -> SecurityEventContextData:
        """Build and return SecurityEventContextData object.

        Returns:
            SecurityEventContextData instance
        """
        # TODO: Add validation
        return self._obj
