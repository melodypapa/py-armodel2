"""CanControllerFdConfigurationRequirements AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    PositiveInteger,
    TimeValue,
)


class CanControllerFdConfigurationRequirements(ARObject):
    """AUTOSAR CanControllerFdConfigurationRequirements."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_number_of_time_quanta_per", None, False, False, any (IntegerBit)),  # maxNumberOfTimeQuantaPer
        ("max_sample", None, True, False, None),  # maxSample
        ("max_sync_jump", None, True, False, None),  # maxSyncJump
        ("max_trcv_delay", None, True, False, None),  # maxTrcvDelay
        ("min_number_of_time_quanta_per", None, False, False, any (IntegerBit)),  # minNumberOfTimeQuantaPer
        ("min_sample_point", None, True, False, None),  # minSamplePoint
        ("min_sync_jump", None, True, False, None),  # minSyncJump
        ("min_trcv_delay", None, True, False, None),  # minTrcvDelay
        ("padding_value", None, True, False, None),  # paddingValue
        ("tx_bit_rate_switch", None, True, False, None),  # txBitRateSwitch
    ]

    def __init__(self) -> None:
        """Initialize CanControllerFdConfigurationRequirements."""
        super().__init__()
        self.max_number_of_time_quanta_per: Optional[Any] = None
        self.max_sample: Optional[Float] = None
        self.max_sync_jump: Optional[Float] = None
        self.max_trcv_delay: Optional[TimeValue] = None
        self.min_number_of_time_quanta_per: Optional[Any] = None
        self.min_sample_point: Optional[Float] = None
        self.min_sync_jump: Optional[Float] = None
        self.min_trcv_delay: Optional[TimeValue] = None
        self.padding_value: Optional[PositiveInteger] = None
        self.tx_bit_rate_switch: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanControllerFdConfigurationRequirements to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerFdConfigurationRequirements":
        """Create CanControllerFdConfigurationRequirements from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanControllerFdConfigurationRequirements instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanControllerFdConfigurationRequirements since parent returns ARObject
        return cast("CanControllerFdConfigurationRequirements", obj)


class CanControllerFdConfigurationRequirementsBuilder:
    """Builder for CanControllerFdConfigurationRequirements."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerFdConfigurationRequirements = CanControllerFdConfigurationRequirements()

    def build(self) -> CanControllerFdConfigurationRequirements:
        """Build and return CanControllerFdConfigurationRequirements object.

        Returns:
            CanControllerFdConfigurationRequirements instance
        """
        # TODO: Add validation
        return self._obj
