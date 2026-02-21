"""CanNmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 683)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CanNmEcu(BusspecificNmEcu):
    """AUTOSAR CanNmEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize CanNmEcu."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize CanNmEcu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanNmEcu, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "CanNmEcu":
        """Deserialize XML element to CanNmEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanNmEcu object
        """
        # Delegate to parent class to handle inherited attributes
        return super(CanNmEcu, cls).deserialize(element)



class CanNmEcuBuilder:
    """Builder for CanNmEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanNmEcu = CanNmEcu()

    def build(self) -> CanNmEcu:
        """Build and return CanNmEcu object.

        Returns:
            CanNmEcu instance
        """
        # TODO: Add validation
        return self._obj
