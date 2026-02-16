"""CanControllerXlConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class CanControllerXlConfiguration(ARObject):
    """AUTOSAR CanControllerXlConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("error_signaling", None, True, False, None),  # errorSignaling
        ("prop_seg", None, True, False, None),  # propSeg
        ("pwm_l", None, True, False, None),  # pwmL
        ("pwm_o", None, True, False, None),  # pwmO
        ("pwm_s", None, True, False, None),  # pwmS
        ("ssp_offset", None, True, False, None),  # sspOffset
        ("sync_jump_width", None, True, False, None),  # syncJumpWidth
        ("time_seg1", None, True, False, None),  # timeSeg1
        ("time_seg2", None, True, False, None),  # timeSeg2
        ("trcv_pwm_mode", None, True, False, None),  # trcvPwmMode
    ]

    def __init__(self) -> None:
        """Initialize CanControllerXlConfiguration."""
        super().__init__()
        self.error_signaling: Optional[Boolean] = None
        self.prop_seg: Optional[PositiveInteger] = None
        self.pwm_l: Optional[PositiveInteger] = None
        self.pwm_o: Optional[PositiveInteger] = None
        self.pwm_s: Optional[PositiveInteger] = None
        self.ssp_offset: Optional[PositiveInteger] = None
        self.sync_jump_width: Optional[PositiveInteger] = None
        self.time_seg1: Optional[PositiveInteger] = None
        self.time_seg2: Optional[PositiveInteger] = None
        self.trcv_pwm_mode: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanControllerXlConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerXlConfiguration":
        """Create CanControllerXlConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanControllerXlConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanControllerXlConfiguration since parent returns ARObject
        return cast("CanControllerXlConfiguration", obj)


class CanControllerXlConfigurationBuilder:
    """Builder for CanControllerXlConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerXlConfiguration = CanControllerXlConfiguration()

    def build(self) -> CanControllerXlConfiguration:
        """Build and return CanControllerXlConfiguration object.

        Returns:
            CanControllerXlConfiguration instance
        """
        # TODO: Add validation
        return self._obj
