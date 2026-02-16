"""TpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)


class TpConfig(FibexElement):
    """AUTOSAR TpConfig."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication_cluster", None, False, False, CommunicationCluster),  # communicationCluster
    ]

    def __init__(self) -> None:
        """Initialize TpConfig."""
        super().__init__()
        self.communication_cluster: Optional[CommunicationCluster] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TpConfig":
        """Create TpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TpConfig since parent returns ARObject
        return cast("TpConfig", obj)


class TpConfigBuilder:
    """Builder for TpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpConfig = TpConfig()

    def build(self) -> TpConfig:
        """Build and return TpConfig object.

        Returns:
            TpConfig instance
        """
        # TODO: Add validation
        return self._obj
