"""CanControllerFdConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class CanControllerFdConfiguration(ARObject):
    """AUTOSAR CanControllerFdConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("padding_value", None, True, False, None),  # paddingValue
        ("prop_seg", None, True, False, None),  # propSeg
        ("ssp_offset", None, True, False, None),  # sspOffset
        ("sync_jump_width", None, True, False, None),  # syncJumpWidth
        ("time_seg1", None, True, False, None),  # timeSeg1
        ("time_seg2", None, True, False, None),  # timeSeg2
        ("tx_bit_rate_switch", None, True, False, None),  # txBitRateSwitch
    ]

    def __init__(self) -> None:
        """Initialize CanControllerFdConfiguration."""
        super().__init__()
        self.padding_value: Optional[PositiveInteger] = None
        self.prop_seg: Optional[PositiveInteger] = None
        self.ssp_offset: Optional[PositiveInteger] = None
        self.sync_jump_width: Optional[PositiveInteger] = None
        self.time_seg1: Optional[PositiveInteger] = None
        self.time_seg2: Optional[PositiveInteger] = None
        self.tx_bit_rate_switch: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanControllerFdConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerFdConfiguration":
        """Create CanControllerFdConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanControllerFdConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanControllerFdConfiguration since parent returns ARObject
        return cast("CanControllerFdConfiguration", obj)


class CanControllerFdConfigurationBuilder:
    """Builder for CanControllerFdConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerFdConfiguration = CanControllerFdConfiguration()

    def build(self) -> CanControllerFdConfiguration:
        """Build and return CanControllerFdConfiguration object.

        Returns:
            CanControllerFdConfiguration instance
        """
        # TODO: Add validation
        return self._obj
