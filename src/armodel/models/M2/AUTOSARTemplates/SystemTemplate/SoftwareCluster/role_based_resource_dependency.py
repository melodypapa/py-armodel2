"""RoleBasedResourceDependency AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class RoleBasedResourceDependency(ARObject):
    """AUTOSAR RoleBasedResourceDependency."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("resource", None, False, False, CpSoftwareCluster),  # resource
        ("role", None, True, False, None),  # role
    ]

    def __init__(self) -> None:
        """Initialize RoleBasedResourceDependency."""
        super().__init__()
        self.resource: Optional[CpSoftwareCluster] = None
        self.role: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RoleBasedResourceDependency to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedResourceDependency":
        """Create RoleBasedResourceDependency from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RoleBasedResourceDependency instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RoleBasedResourceDependency since parent returns ARObject
        return cast("RoleBasedResourceDependency", obj)


class RoleBasedResourceDependencyBuilder:
    """Builder for RoleBasedResourceDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedResourceDependency = RoleBasedResourceDependency()

    def build(self) -> RoleBasedResourceDependency:
        """Build and return RoleBasedResourceDependency object.

        Returns:
            RoleBasedResourceDependency instance
        """
        # TODO: Add validation
        return self._obj
