"""DoIpEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 471)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    DoIpEntityRoleEnum,
)


class DoIpEntity(ARObject):
    """AUTOSAR DoIpEntity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "do_ip_entity_role_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DoIpEntityRoleEnum,
        ),  # doIpEntityRoleEnum
    }

    def __init__(self) -> None:
        """Initialize DoIpEntity."""
        super().__init__()
        self.do_ip_entity_role_enum: Optional[DoIpEntityRoleEnum] = None


class DoIpEntityBuilder:
    """Builder for DoIpEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpEntity = DoIpEntity()

    def build(self) -> DoIpEntity:
        """Build and return DoIpEntity object.

        Returns:
            DoIpEntity instance
        """
        # TODO: Add validation
        return self._obj
