"""DdsCpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_domain import (
    DdsCpDomain,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)


class DdsCpConfig(ARElement):
    """AUTOSAR DdsCpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dds_domains", None, False, True, DdsCpDomain),  # ddsDomains
        ("dds_qos_profiles", None, False, True, DdsCpQosProfile),  # ddsQosProfiles
    ]

    def __init__(self) -> None:
        """Initialize DdsCpConfig."""
        super().__init__()
        self.dds_domains: list[DdsCpDomain] = []
        self.dds_qos_profiles: list[DdsCpQosProfile] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsCpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpConfig":
        """Create DdsCpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsCpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsCpConfig since parent returns ARObject
        return cast("DdsCpConfig", obj)


class DdsCpConfigBuilder:
    """Builder for DdsCpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpConfig = DdsCpConfig()

    def build(self) -> DdsCpConfig:
        """Build and return DdsCpConfig object.

        Returns:
            DdsCpConfig instance
        """
        # TODO: Add validation
        return self._obj
