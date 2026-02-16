"""MacSecLocalKayProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_global_kay_props import (
    MacSecGlobalKayProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_kay_participant import (
    MacSecKayParticipant,
)


class MacSecLocalKayProps(ARObject):
    """AUTOSAR MacSecLocalKayProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination_mac", None, True, False, None),  # destinationMac
        ("global_kay_props", None, False, False, MacSecGlobalKayProps),  # globalKayProps
        ("key_server", None, True, False, None),  # keyServer
        ("mka_participants", None, False, True, MacSecKayParticipant),  # mkaParticipants
        ("role", None, False, False, MacSecRoleEnum),  # role
        ("source_mac", None, True, False, None),  # sourceMac
    ]

    def __init__(self) -> None:
        """Initialize MacSecLocalKayProps."""
        super().__init__()
        self.destination_mac: Optional[MacAddressString] = None
        self.global_kay_props: Optional[MacSecGlobalKayProps] = None
        self.key_server: Optional[PositiveInteger] = None
        self.mka_participants: list[MacSecKayParticipant] = []
        self.role: Optional[MacSecRoleEnum] = None
        self.source_mac: Optional[MacAddressString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MacSecLocalKayProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecLocalKayProps":
        """Create MacSecLocalKayProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MacSecLocalKayProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MacSecLocalKayProps since parent returns ARObject
        return cast("MacSecLocalKayProps", obj)


class MacSecLocalKayPropsBuilder:
    """Builder for MacSecLocalKayProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecLocalKayProps = MacSecLocalKayProps()

    def build(self) -> MacSecLocalKayProps:
        """Build and return MacSecLocalKayProps object.

        Returns:
            MacSecLocalKayProps instance
        """
        # TODO: Add validation
        return self._obj
