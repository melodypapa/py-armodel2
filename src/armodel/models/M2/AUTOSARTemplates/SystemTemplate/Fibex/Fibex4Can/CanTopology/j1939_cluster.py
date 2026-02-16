"""J1939Cluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class J1939Cluster(ARObject):
    """AUTOSAR J1939Cluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("network_id", None, True, False, None),  # networkId
        ("request2_support", None, True, False, None),  # request2Support
        ("uses_address", None, True, False, None),  # usesAddress
    ]

    def __init__(self) -> None:
        """Initialize J1939Cluster."""
        super().__init__()
        self.network_id: Optional[PositiveInteger] = None
        self.request2_support: Optional[Boolean] = None
        self.uses_address: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939Cluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939Cluster":
        """Create J1939Cluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939Cluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939Cluster since parent returns ARObject
        return cast("J1939Cluster", obj)


class J1939ClusterBuilder:
    """Builder for J1939Cluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939Cluster = J1939Cluster()

    def build(self) -> J1939Cluster:
        """Build and return J1939Cluster object.

        Returns:
            J1939Cluster instance
        """
        # TODO: Add validation
        return self._obj
