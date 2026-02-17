"""J1939NodeName AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 691)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class J1939NodeName(ARObject):
    """AUTOSAR J1939NodeName."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "arbitrary_address": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # arbitraryAddress
        "ecu_instance": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ecuInstance
        "function": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # function
        "function_instance": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # functionInstance
        "identitiy_number": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # identitiyNumber
        "industry_group": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # industryGroup
        "manufacturer_code": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # manufacturerCode
        "vehicle_system": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vehicleSystem
        "vehicle_system_instance": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vehicleSystemInstance
    }

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
