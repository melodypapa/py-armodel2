"""CommunicationControllerMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 182)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    communication_controller_ref: Optional[ARRef]
    hw_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize CommunicationControllerMapping."""
        super().__init__()
        self.communication_controller_ref: Optional[ARRef] = None
        self.hw_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CommunicationControllerMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommunicationControllerMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_controller_ref
        if self.communication_controller_ref is not None:
            serialized = SerializationHelper.serialize_item(self.communication_controller_ref, "CommunicationController")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CONTROLLER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hw_ref
        if self.hw_ref is not None:
            serialized = SerializationHelper.serialize_item(self.hw_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-REF")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommunicationControllerMapping, cls).deserialize(element)

        # Parse communication_controller_ref
        child = SerializationHelper.find_child_element(element, "COMMUNICATION-CONTROLLER-REF")
        if child is not None:
            communication_controller_ref_value = ARRef.deserialize(child)
            obj.communication_controller_ref = communication_controller_ref_value

        # Parse hw_ref
        child = SerializationHelper.find_child_element(element, "HW-REF")
        if child is not None:
            hw_ref_value = ARRef.deserialize(child)
            obj.hw_ref = hw_ref_value

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
