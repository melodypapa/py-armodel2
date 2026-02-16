"""DdsCpConsumedServiceInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AnyVersionString,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)


class DdsCpConsumedServiceInstance(DdsCpServiceInstance):
    """AUTOSAR DdsCpConsumedServiceInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("consumed_ddses", None, False, True, DdsCpServiceInstance),  # consumedDdses
        ("local_unicast", None, False, False, ApplicationEndpoint),  # localUnicast
        ("minor_version", None, True, False, None),  # minorVersion
        ("static_remote", None, False, False, ApplicationEndpoint),  # staticRemote
    ]

    def __init__(self) -> None:
        """Initialize DdsCpConsumedServiceInstance."""
        super().__init__()
        self.consumed_ddses: list[DdsCpServiceInstance] = []
        self.local_unicast: Optional[ApplicationEndpoint] = None
        self.minor_version: Optional[AnyVersionString] = None
        self.static_remote: Optional[ApplicationEndpoint] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsCpConsumedServiceInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpConsumedServiceInstance":
        """Create DdsCpConsumedServiceInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsCpConsumedServiceInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsCpConsumedServiceInstance since parent returns ARObject
        return cast("DdsCpConsumedServiceInstance", obj)


class DdsCpConsumedServiceInstanceBuilder:
    """Builder for DdsCpConsumedServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpConsumedServiceInstance = DdsCpConsumedServiceInstance()

    def build(self) -> DdsCpConsumedServiceInstance:
        """Build and return DdsCpConsumedServiceInstance object.

        Returns:
            DdsCpConsumedServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
