"""ApplicationPartition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ApplicationPartition(ARElement):
    """AUTOSAR ApplicationPartition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ApplicationPartition."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize ApplicationPartition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationPartition, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "ApplicationPartition":
        """Deserialize XML element to ApplicationPartition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationPartition object
        """
        # Delegate to parent class to handle inherited attributes
        return super(ApplicationPartition, cls).deserialize(element)



class ApplicationPartitionBuilder:
    """Builder for ApplicationPartition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationPartition = ApplicationPartition()

    def build(self) -> ApplicationPartition:
        """Build and return ApplicationPartition object.

        Returns:
            ApplicationPartition instance
        """
        # TODO: Add validation
        return self._obj
