"""DoIpGidNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 805)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2019)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
    DoIpServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DoIpGidNeeds(DoIpServiceNeeds):
    """AUTOSAR DoIpGidNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DoIpGidNeeds."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DoIpGidNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpGidNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpGidNeeds":
        """Deserialize XML element to DoIpGidNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpGidNeeds object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DoIpGidNeeds, cls).deserialize(element)



class DoIpGidNeedsBuilder:
    """Builder for DoIpGidNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpGidNeeds = DoIpGidNeeds()

    def build(self) -> DoIpGidNeeds:
        """Build and return DoIpGidNeeds object.

        Returns:
            DoIpGidNeeds instance
        """
        # TODO: Add validation
        return self._obj
