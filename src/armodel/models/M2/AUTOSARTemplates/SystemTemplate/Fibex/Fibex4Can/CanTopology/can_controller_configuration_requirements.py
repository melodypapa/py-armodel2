"""CanControllerConfigurationRequirements AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_controller_attributes import (
    AbstractCanCommunicationControllerAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class CanControllerConfigurationRequirements(AbstractCanCommunicationControllerAttributes):
    """AUTOSAR CanControllerConfigurationRequirements."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_number_of_time_quanta_per", None, False, False, any (IntegerBit)),  # maxNumberOfTimeQuantaPer
        ("max_sample", None, True, False, None),  # maxSample
        ("max_sync_jump", None, True, False, None),  # maxSyncJump
        ("min_number_of_time_quanta_per", None, False, False, any (IntegerBit)),  # minNumberOfTimeQuantaPer
        ("min_sample_point", None, True, False, None),  # minSamplePoint
        ("min_sync_jump", None, True, False, None),  # minSyncJump
    ]

    def __init__(self) -> None:
        """Initialize CanControllerConfigurationRequirements."""
        super().__init__()
        self.max_number_of_time_quanta_per: Optional[Any] = None
        self.max_sample: Optional[Float] = None
        self.max_sync_jump: Optional[Float] = None
        self.min_number_of_time_quanta_per: Optional[Any] = None
        self.min_sample_point: Optional[Float] = None
        self.min_sync_jump: Optional[Float] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanControllerConfigurationRequirements to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerConfigurationRequirements":
        """Create CanControllerConfigurationRequirements from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanControllerConfigurationRequirements instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanControllerConfigurationRequirements since parent returns ARObject
        return cast("CanControllerConfigurationRequirements", obj)


class CanControllerConfigurationRequirementsBuilder:
    """Builder for CanControllerConfigurationRequirements."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerConfigurationRequirements = CanControllerConfigurationRequirements()

    def build(self) -> CanControllerConfigurationRequirements:
        """Build and return CanControllerConfigurationRequirements object.

        Returns:
            CanControllerConfigurationRequirements instance
        """
        # TODO: Add validation
        return self._obj
