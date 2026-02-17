"""MacSecLocalKayProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "destination_mac": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # destinationMac
        "global_kay_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MacSecGlobalKayProps,
        ),  # globalKayProps
        "key_server": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # keyServer
        "mka_participants": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=MacSecKayParticipant,
        ),  # mkaParticipants
        "role": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MacSecRoleEnum,
        ),  # role
        "source_mac": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sourceMac
    }

    def __init__(self) -> None:
        """Initialize MacSecLocalKayProps."""
        super().__init__()
        self.destination_mac: Optional[MacAddressString] = None
        self.global_kay_props: Optional[MacSecGlobalKayProps] = None
        self.key_server: Optional[PositiveInteger] = None
        self.mka_participants: list[MacSecKayParticipant] = []
        self.role: Optional[MacSecRoleEnum] = None
        self.source_mac: Optional[MacAddressString] = None


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
