"""DdsCpProvidedServiceInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)


class DdsCpProvidedServiceInstance(DdsCpServiceInstance):
    """AUTOSAR DdsCpProvidedServiceInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("local_unicast", None, False, False, ApplicationEndpoint),  # localUnicast
        ("minor_version", None, True, False, None),  # minorVersion
        ("provided_ddses", None, False, True, DdsCpServiceInstance),  # providedDdses
        ("static_remotes", None, False, True, ApplicationEndpoint),  # staticRemotes
    ]

    def __init__(self) -> None:
        """Initialize DdsCpProvidedServiceInstance."""
        super().__init__()
        self.local_unicast: Optional[ApplicationEndpoint] = None
        self.minor_version: Optional[PositiveInteger] = None
        self.provided_ddses: list[DdsCpServiceInstance] = []
        self.static_remotes: list[ApplicationEndpoint] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsCpProvidedServiceInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpProvidedServiceInstance":
        """Create DdsCpProvidedServiceInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsCpProvidedServiceInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsCpProvidedServiceInstance since parent returns ARObject
        return cast("DdsCpProvidedServiceInstance", obj)


class DdsCpProvidedServiceInstanceBuilder:
    """Builder for DdsCpProvidedServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpProvidedServiceInstance = DdsCpProvidedServiceInstance()

    def build(self) -> DdsCpProvidedServiceInstance:
        """Build and return DdsCpProvidedServiceInstance object.

        Returns:
            DdsCpProvidedServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
