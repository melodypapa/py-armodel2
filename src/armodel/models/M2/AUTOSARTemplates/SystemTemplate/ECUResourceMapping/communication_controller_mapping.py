"""CommunicationControllerMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 182)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_controller import (
    CommunicationController,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)


class CommunicationControllerMapping(ARObject):
    """AUTOSAR CommunicationControllerMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication_controller: Optional[CommunicationController]
    hw: Optional[HwElement]
    def __init__(self) -> None:
        """Initialize CommunicationControllerMapping."""
        super().__init__()
        self.communication_controller: Optional[CommunicationController] = None
        self.hw: Optional[HwElement] = None

    def serialize(self) -> ET.Element:
        """Serialize CommunicationControllerMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize communication_controller
        if self.communication_controller is not None:
            serialized = ARObject._serialize_item(self.communication_controller, "CommunicationController")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CONTROLLER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hw
        if self.hw is not None:
            serialized = ARObject._serialize_item(self.hw, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationControllerMapping":
        """Deserialize XML element to CommunicationControllerMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationControllerMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse communication_controller
        child = ARObject._find_child_element(element, "COMMUNICATION-CONTROLLER")
        if child is not None:
            communication_controller_value = ARObject._deserialize_by_tag(child, "CommunicationController")
            obj.communication_controller = communication_controller_value

        # Parse hw
        child = ARObject._find_child_element(element, "HW")
        if child is not None:
            hw_value = ARObject._deserialize_by_tag(child, "HwElement")
            obj.hw = hw_value

        return obj



class CommunicationControllerMappingBuilder:
    """Builder for CommunicationControllerMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationControllerMapping = CommunicationControllerMapping()

    def build(self) -> CommunicationControllerMapping:
        """Build and return CommunicationControllerMapping object.

        Returns:
            CommunicationControllerMapping instance
        """
        # TODO: Add validation
        return self._obj
