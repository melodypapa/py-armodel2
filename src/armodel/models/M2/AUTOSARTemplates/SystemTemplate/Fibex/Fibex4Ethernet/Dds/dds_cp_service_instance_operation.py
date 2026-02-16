"""DdsCpServiceInstanceOperation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DdsCpServiceInstanceOperation(ARObject):
    """AUTOSAR DdsCpServiceInstanceOperation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dds_operation", None, False, False, PduTriggering),  # ddsOperation
    ]

    def __init__(self) -> None:
        """Initialize DdsCpServiceInstanceOperation."""
        super().__init__()
        self.dds_operation: Optional[PduTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsCpServiceInstanceOperation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpServiceInstanceOperation":
        """Create DdsCpServiceInstanceOperation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsCpServiceInstanceOperation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsCpServiceInstanceOperation since parent returns ARObject
        return cast("DdsCpServiceInstanceOperation", obj)


class DdsCpServiceInstanceOperationBuilder:
    """Builder for DdsCpServiceInstanceOperation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpServiceInstanceOperation = DdsCpServiceInstanceOperation()

    def build(self) -> DdsCpServiceInstanceOperation:
        """Build and return DdsCpServiceInstanceOperation object.

        Returns:
            DdsCpServiceInstanceOperation instance
        """
        # TODO: Add validation
        return self._obj
