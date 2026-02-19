"""DoIpEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 471)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    DoIpEntityRoleEnum,
)


class DoIpEntity(ARObject):
    """AUTOSAR DoIpEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    do_ip_entity_role_enum: Optional[DoIpEntityRoleEnum]
    def __init__(self) -> None:
        """Initialize DoIpEntity."""
        super().__init__()
        self.do_ip_entity_role_enum: Optional[DoIpEntityRoleEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpEntity":
        """Deserialize XML element to DoIpEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpEntity object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse do_ip_entity_role_enum
        child = ARObject._find_child_element(element, "DO-IP-ENTITY-ROLE-ENUM")
        if child is not None:
            do_ip_entity_role_enum_value = child.text
            obj.do_ip_entity_role_enum = do_ip_entity_role_enum_value

        return obj



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
