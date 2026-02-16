"""CpSoftwareClusterResource AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.role_based_resource_dependency import (
    RoleBasedResourceDependency,
)


class CpSoftwareClusterResource(Identifiable):
    """AUTOSAR CpSoftwareClusterResource."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dependents", None, False, True, RoleBasedResourceDependency),  # dependents
        ("global_resource", None, True, False, None),  # globalResource
        ("is_mandatory", None, True, False, None),  # isMandatory
    ]

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResource."""
        super().__init__()
        self.dependents: list[RoleBasedResourceDependency] = []
        self.global_resource: Optional[PositiveInteger] = None
        self.is_mandatory: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSoftwareClusterResource to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterResource":
        """Create CpSoftwareClusterResource from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSoftwareClusterResource instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSoftwareClusterResource since parent returns ARObject
        return cast("CpSoftwareClusterResource", obj)


class CpSoftwareClusterResourceBuilder:
    """Builder for CpSoftwareClusterResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterResource = CpSoftwareClusterResource()

    def build(self) -> CpSoftwareClusterResource:
        """Build and return CpSoftwareClusterResource object.

        Returns:
            CpSoftwareClusterResource instance
        """
        # TODO: Add validation
        return self._obj
