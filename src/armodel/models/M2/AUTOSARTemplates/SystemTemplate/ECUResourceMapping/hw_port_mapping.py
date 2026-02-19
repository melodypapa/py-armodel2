"""HwPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 183)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    communication_connector: Optional[CommunicationConnector]
    hw_pin_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize HwPortMapping."""
        super().__init__()
        self.communication_connector: Optional[CommunicationConnector] = None
        self.hw_pin_group_ref: Optional[ARRef] = None
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

        # Parse communication_connector
        child = ARObject._find_child_element(element, "COMMUNICATION-CONNECTOR")
        if child is not None:
            communication_connector_value = ARObject._deserialize_by_tag(child, "CommunicationConnector")
            obj.communication_connector = communication_connector_value

        # Parse hw_pin_group_ref
        child = ARObject._find_child_element(element, "HW-PIN-GROUP")
        if child is not None:
            hw_pin_group_ref_value = ARObject._deserialize_by_tag(child, "HwPinGroup")
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
