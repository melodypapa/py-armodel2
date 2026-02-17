"""EthernetWakeupSleepOnDatalineConfigSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)


class EthernetWakeupSleepOnDatalineConfigSet(FibexElement):
    """AUTOSAR EthernetWakeupSleepOnDatalineConfigSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ethernets": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # ethernets
    }

    def __init__(self) -> None:
        """Initialize EthernetWakeupSleepOnDatalineConfigSet."""
        super().__init__()
        self.ethernets: list[Any] = []


class EthernetWakeupSleepOnDatalineConfigSetBuilder:
    """Builder for EthernetWakeupSleepOnDatalineConfigSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetWakeupSleepOnDatalineConfigSet = EthernetWakeupSleepOnDatalineConfigSet()

    def build(self) -> EthernetWakeupSleepOnDatalineConfigSet:
        """Build and return EthernetWakeupSleepOnDatalineConfigSet object.

        Returns:
            EthernetWakeupSleepOnDatalineConfigSet instance
        """
        # TODO: Add validation
        return self._obj
