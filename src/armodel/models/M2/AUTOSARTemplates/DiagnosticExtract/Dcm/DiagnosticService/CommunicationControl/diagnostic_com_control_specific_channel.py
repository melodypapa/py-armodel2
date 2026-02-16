"""DiagnosticComControlSpecificChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)


class DiagnosticComControlSpecificChannel(ARObject):
    """AUTOSAR DiagnosticComControlSpecificChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("specific_channel", None, False, False, CommunicationCluster),  # specificChannel
        ("specific_physical", None, False, False, any (EthernetPhysical)),  # specificPhysical
        ("subnet_number", None, True, False, None),  # subnetNumber
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticComControlSpecificChannel."""
        super().__init__()
        self.specific_channel: Optional[CommunicationCluster] = None
        self.specific_physical: Optional[Any] = None
        self.subnet_number: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticComControlSpecificChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlSpecificChannel":
        """Create DiagnosticComControlSpecificChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticComControlSpecificChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticComControlSpecificChannel since parent returns ARObject
        return cast("DiagnosticComControlSpecificChannel", obj)


class DiagnosticComControlSpecificChannelBuilder:
    """Builder for DiagnosticComControlSpecificChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControlSpecificChannel = DiagnosticComControlSpecificChannel()

    def build(self) -> DiagnosticComControlSpecificChannel:
        """Build and return DiagnosticComControlSpecificChannel object.

        Returns:
            DiagnosticComControlSpecificChannel instance
        """
        # TODO: Add validation
        return self._obj
