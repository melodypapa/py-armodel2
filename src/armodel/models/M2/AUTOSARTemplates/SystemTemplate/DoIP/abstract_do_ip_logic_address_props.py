"""AbstractDoIpLogicAddressProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 556)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class AbstractDoIpLogicAddressProps(Identifiable, ABC):
    """AUTOSAR AbstractDoIpLogicAddressProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractDoIpLogicAddressProps."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize AbstractDoIpLogicAddressProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractDoIpLogicAddressProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractDoIpLogicAddressProps":
        """Deserialize XML element to AbstractDoIpLogicAddressProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractDoIpLogicAddressProps object
        """
        # Delegate to parent class to handle inherited attributes
        return super(AbstractDoIpLogicAddressProps, cls).deserialize(element)



class AbstractDoIpLogicAddressPropsBuilder:
    """Builder for AbstractDoIpLogicAddressProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractDoIpLogicAddressProps = AbstractDoIpLogicAddressProps()

    def build(self) -> AbstractDoIpLogicAddressProps:
        """Build and return AbstractDoIpLogicAddressProps object.

        Returns:
            AbstractDoIpLogicAddressProps instance
        """
        # TODO: Add validation
        return self._obj
