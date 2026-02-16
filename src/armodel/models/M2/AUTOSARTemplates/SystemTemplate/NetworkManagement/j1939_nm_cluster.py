"""J1939NmCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class J1939NmCluster(NmCluster):
    """AUTOSAR J1939NmCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("address_claim", None, True, False, None),  # addressClaim
        ("uses_dynamic", None, True, False, None),  # usesDynamic
    ]

    def __init__(self) -> None:
        """Initialize J1939NmCluster."""
        super().__init__()
        self.address_claim: Optional[Boolean] = None
        self.uses_dynamic: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939NmCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939NmCluster":
        """Create J1939NmCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939NmCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939NmCluster since parent returns ARObject
        return cast("J1939NmCluster", obj)


class J1939NmClusterBuilder:
    """Builder for J1939NmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NmCluster = J1939NmCluster()

    def build(self) -> J1939NmCluster:
        """Build and return J1939NmCluster object.

        Returns:
            J1939NmCluster instance
        """
        # TODO: Add validation
        return self._obj
