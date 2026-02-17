"""J1939NodeName AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 691)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class J1939NodeName(ARObject):
    """AUTOSAR J1939NodeName."""

    arbitrary_address: Optional[Any]
    ecu_instance: Optional[Integer]
    function: Optional[Integer]
    function_instance: Optional[Integer]
    identitiy_number: Optional[Integer]
    industry_group: Optional[Integer]
    manufacturer_code: Optional[Integer]
    vehicle_system: Optional[Integer]
    vehicle_system_instance: Optional[Integer]
    def __init__(self) -> None:
        """Initialize J1939NodeName."""
        super().__init__()
        self.arbitrary_address: Optional[Any] = None
        self.ecu_instance: Optional[Integer] = None
        self.function: Optional[Integer] = None
        self.function_instance: Optional[Integer] = None
        self.identitiy_number: Optional[Integer] = None
        self.industry_group: Optional[Integer] = None
        self.manufacturer_code: Optional[Integer] = None
        self.vehicle_system: Optional[Integer] = None
        self.vehicle_system_instance: Optional[Integer] = None


class J1939NodeNameBuilder:
    """Builder for J1939NodeName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NodeName = J1939NodeName()

    def build(self) -> J1939NodeName:
        """Build and return J1939NodeName object.

        Returns:
            J1939NodeName instance
        """
        # TODO: Add validation
        return self._obj
