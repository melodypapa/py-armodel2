"""VlanConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class VlanConfig(Identifiable):
    """AUTOSAR VlanConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("vlan_identifier", None, True, False, None),  # vlanIdentifier
    ]

    def __init__(self) -> None:
        """Initialize VlanConfig."""
        super().__init__()
        self.vlan_identifier: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert VlanConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VlanConfig":
        """Create VlanConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            VlanConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to VlanConfig since parent returns ARObject
        return cast("VlanConfig", obj)


class VlanConfigBuilder:
    """Builder for VlanConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VlanConfig = VlanConfig()

    def build(self) -> VlanConfig:
        """Build and return VlanConfig object.

        Returns:
            VlanConfig instance
        """
        # TODO: Add validation
        return self._obj
