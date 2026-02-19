"""MacSecLocalKayProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    MacSecRoleEnum,
)
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_mac: Optional[MacAddressString]
    global_kay_props: Optional[MacSecGlobalKayProps]
    key_server: Optional[PositiveInteger]
    mka_participants: list[MacSecKayParticipant]
    role: Optional[MacSecRoleEnum]
    source_mac: Optional[MacAddressString]
    def __init__(self) -> None:
        """Initialize MacSecLocalKayProps."""
        super().__init__()
        self.destination_mac: Optional[MacAddressString] = None
        self.global_kay_props: Optional[MacSecGlobalKayProps] = None
        self.key_server: Optional[PositiveInteger] = None
        self.mka_participants: list[MacSecKayParticipant] = []
        self.role: Optional[MacSecRoleEnum] = None
        self.source_mac: Optional[MacAddressString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecLocalKayProps":
        """Deserialize XML element to MacSecLocalKayProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecLocalKayProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse destination_mac
        child = ARObject._find_child_element(element, "DESTINATION-MAC")
        if child is not None:
            destination_mac_value = child.text
            obj.destination_mac = destination_mac_value

        # Parse global_kay_props
        child = ARObject._find_child_element(element, "GLOBAL-KAY-PROPS")
        if child is not None:
            global_kay_props_value = ARObject._deserialize_by_tag(child, "MacSecGlobalKayProps")
            obj.global_kay_props = global_kay_props_value

        # Parse key_server
        child = ARObject._find_child_element(element, "KEY-SERVER")
        if child is not None:
            key_server_value = child.text
            obj.key_server = key_server_value

        # Parse mka_participants (list from container "MKA-PARTICIPANTS")
        obj.mka_participants = []
        container = ARObject._find_child_element(element, "MKA-PARTICIPANTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mka_participants.append(child_value)

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = MacSecRoleEnum.deserialize(child)
            obj.role = role_value

        # Parse source_mac
        child = ARObject._find_child_element(element, "SOURCE-MAC")
        if child is not None:
            source_mac_value = child.text
            obj.source_mac = source_mac_value

        return obj



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
