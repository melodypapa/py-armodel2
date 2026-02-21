"""J1939NmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 694)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class J1939NmEcu(BusspecificNmEcu):
    """AUTOSAR J1939NmEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize J1939NmEcu."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize J1939NmEcu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939NmEcu, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "J1939NmEcu":
        """Deserialize XML element to J1939NmEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939NmEcu object
        """
        # Delegate to parent class to handle inherited attributes
        return super(J1939NmEcu, cls).deserialize(element)



class J1939NmEcuBuilder:
    """Builder for J1939NmEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NmEcu = J1939NmEcu()

    def build(self) -> J1939NmEcu:
        """Build and return J1939NmEcu object.

        Returns:
            J1939NmEcu instance
        """
        # TODO: Add validation
        return self._obj
