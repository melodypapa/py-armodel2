"""PortInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 119)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2046)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class PortInterfaceMapping(Identifiable, ABC):
    """AUTOSAR PortInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize PortInterfaceMapping."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize PortInterfaceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortInterfaceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortInterfaceMapping":
        """Deserialize XML element to PortInterfaceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortInterfaceMapping object
        """
        # Delegate to parent class to handle inherited attributes
        return super(PortInterfaceMapping, cls).deserialize(element)



class PortInterfaceMappingBuilder:
    """Builder for PortInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortInterfaceMapping = PortInterfaceMapping()

    def build(self) -> PortInterfaceMapping:
        """Build and return PortInterfaceMapping object.

        Returns:
            PortInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
