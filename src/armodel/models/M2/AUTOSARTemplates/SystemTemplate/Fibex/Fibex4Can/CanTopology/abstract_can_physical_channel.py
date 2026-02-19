"""AbstractCanPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class AbstractCanPhysicalChannel(PhysicalChannel, ABC):
    """AUTOSAR AbstractCanPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractCanPhysicalChannel."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize AbstractCanPhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractCanPhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanPhysicalChannel":
        """Deserialize XML element to AbstractCanPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractCanPhysicalChannel object
        """
        # Delegate to parent class to handle inherited attributes
        return super(AbstractCanPhysicalChannel, cls).deserialize(element)



class AbstractCanPhysicalChannelBuilder:
    """Builder for AbstractCanPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanPhysicalChannel = AbstractCanPhysicalChannel()

    def build(self) -> AbstractCanPhysicalChannel:
        """Build and return AbstractCanPhysicalChannel object.

        Returns:
            AbstractCanPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
