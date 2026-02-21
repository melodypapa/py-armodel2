"""HwPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 183)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)


class HwPortMapping(ARObject):
    """AUTOSAR HwPortMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication_connector_ref: Optional[ARRef]
    hw_pin_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize HwPortMapping."""
        super().__init__()
        self.communication_connector_ref: Optional[ARRef] = None
        self.hw_pin_group_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize HwPortMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize communication_connector_ref
        if self.communication_connector_ref is not None:
            serialized = SerializationHelper.serialize_item(self.communication_connector_ref, "CommunicationConnector")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CONNECTOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hw_pin_group_ref
        if self.hw_pin_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.hw_pin_group_ref, "HwPinGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-PIN-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPortMapping":
        """Deserialize XML element to HwPortMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPortMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse communication_connector_ref
        child = SerializationHelper.find_child_element(element, "COMMUNICATION-CONNECTOR-REF")
        if child is not None:
            communication_connector_ref_value = ARRef.deserialize(child)
            obj.communication_connector_ref = communication_connector_ref_value

        # Parse hw_pin_group_ref
        child = SerializationHelper.find_child_element(element, "HW-PIN-GROUP-REF")
        if child is not None:
            hw_pin_group_ref_value = ARRef.deserialize(child)
            obj.hw_pin_group_ref = hw_pin_group_ref_value

        return obj



class HwPortMappingBuilder:
    """Builder for HwPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPortMapping = HwPortMapping()

    def build(self) -> HwPortMapping:
        """Build and return HwPortMapping object.

        Returns:
            HwPortMapping instance
        """
        # TODO: Add validation
        return self._obj
