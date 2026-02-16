"""CanControllerXlConfigurationRequirements AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    PositiveInteger,
    TimeValue,
)


class CanControllerXlConfigurationRequirements(ARObject):
    """AUTOSAR CanControllerXlConfigurationRequirements."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("error_signaling", None, True, False, None),  # errorSignaling
        ("max_number_of_time_quanta_per", None, False, False, any (IntegerBit)),  # maxNumberOfTimeQuantaPer
        ("max_pwm_l", None, True, False, None),  # maxPwmL
        ("max_pwm_o", None, True, False, None),  # maxPwmO
        ("max_pwm_s", None, True, False, None),  # maxPwmS
        ("max_sample", None, True, False, None),  # maxSample
        ("max_sync_jump", None, True, False, None),  # maxSyncJump
        ("max_trcv_delay", None, True, False, None),  # maxTrcvDelay
        ("min_number_of_time_quanta_per", None, False, False, any (IntegerBit)),  # minNumberOfTimeQuantaPer
        ("min_pwm_l", None, True, False, None),  # minPwmL
        ("min_pwm_o", None, True, False, None),  # minPwmO
        ("min_pwm_s", None, True, False, None),  # minPwmS
        ("min_sample_point", None, True, False, None),  # minSamplePoint
        ("min_sync_jump", None, True, False, None),  # minSyncJump
        ("min_trcv_delay", None, True, False, None),  # minTrcvDelay
        ("trcv_pwm_mode", None, True, False, None),  # trcvPwmMode
    ]

    def __init__(self) -> None:
        """Initialize CanControllerXlConfigurationRequirements."""
        super().__init__()
        self.error_signaling: Optional[Boolean] = None
        self.max_number_of_time_quanta_per: Optional[Any] = None
        self.max_pwm_l: Optional[PositiveInteger] = None
        self.max_pwm_o: Optional[PositiveInteger] = None
        self.max_pwm_s: Optional[PositiveInteger] = None
        self.max_sample: Optional[Float] = None
        self.max_sync_jump: Optional[Float] = None
        self.max_trcv_delay: Optional[TimeValue] = None
        self.min_number_of_time_quanta_per: Optional[Any] = None
        self.min_pwm_l: Optional[PositiveInteger] = None
        self.min_pwm_o: Optional[PositiveInteger] = None
        self.min_pwm_s: Optional[PositiveInteger] = None
        self.min_sample_point: Optional[Float] = None
        self.min_sync_jump: Optional[Float] = None
        self.min_trcv_delay: Optional[TimeValue] = None
        self.trcv_pwm_mode: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanControllerXlConfigurationRequirements to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerXlConfigurationRequirements":
        """Create CanControllerXlConfigurationRequirements from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanControllerXlConfigurationRequirements instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanControllerXlConfigurationRequirements since parent returns ARObject
        return cast("CanControllerXlConfigurationRequirements", obj)


class CanControllerXlConfigurationRequirementsBuilder:
    """Builder for CanControllerXlConfigurationRequirements."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerXlConfigurationRequirements = CanControllerXlConfigurationRequirements()

    def build(self) -> CanControllerXlConfigurationRequirements:
        """Build and return CanControllerXlConfigurationRequirements object.

        Returns:
            CanControllerXlConfigurationRequirements instance
        """
        # TODO: Add validation
        return self._obj
