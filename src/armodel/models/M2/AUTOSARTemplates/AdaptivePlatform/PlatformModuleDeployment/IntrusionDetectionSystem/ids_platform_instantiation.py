"""IdsPlatformInstantiation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.AdaptiveModule.platform_module_ethernet_endpoint_configuration import (
    PlatformModuleEthernetEndpointConfiguration,
)


class IdsPlatformInstantiation(Identifiable):
    """AUTOSAR IdsPlatformInstantiation."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("networks", None, False, True, PlatformModuleEthernetEndpointConfiguration),  # networks
        ("time_base_resource", None, False, False, any (TimeBaseResource)),  # timeBaseResource
    ]

    def __init__(self) -> None:
        """Initialize IdsPlatformInstantiation."""
        super().__init__()
        self.networks: list[PlatformModuleEthernetEndpointConfiguration] = []
        self.time_base_resource: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IdsPlatformInstantiation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsPlatformInstantiation":
        """Create IdsPlatformInstantiation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IdsPlatformInstantiation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IdsPlatformInstantiation since parent returns ARObject
        return cast("IdsPlatformInstantiation", obj)


class IdsPlatformInstantiationBuilder:
    """Builder for IdsPlatformInstantiation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsPlatformInstantiation = IdsPlatformInstantiation()

    def build(self) -> IdsPlatformInstantiation:
        """Build and return IdsPlatformInstantiation object.

        Returns:
            IdsPlatformInstantiation instance
        """
        # TODO: Add validation
        return self._obj
