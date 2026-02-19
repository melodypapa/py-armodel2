"""J1939DcmDm19Support AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 831)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class J1939DcmDm19Support(ServiceNeeds):
    """AUTOSAR J1939DcmDm19Support."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize J1939DcmDm19Support."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize J1939DcmDm19Support to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939DcmDm19Support, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939DcmDm19Support":
        """Deserialize XML element to J1939DcmDm19Support object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939DcmDm19Support object
        """
        # Delegate to parent class to handle inherited attributes
        return super(J1939DcmDm19Support, cls).deserialize(element)



class J1939DcmDm19SupportBuilder:
    """Builder for J1939DcmDm19Support."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939DcmDm19Support = J1939DcmDm19Support()

    def build(self) -> J1939DcmDm19Support:
        """Build and return J1939DcmDm19Support object.

        Returns:
            J1939DcmDm19Support instance
        """
        # TODO: Add validation
        return self._obj
