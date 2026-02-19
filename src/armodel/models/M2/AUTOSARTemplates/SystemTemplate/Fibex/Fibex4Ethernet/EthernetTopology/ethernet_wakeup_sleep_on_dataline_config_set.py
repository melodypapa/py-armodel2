"""EthernetWakeupSleepOnDatalineConfigSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class EthernetWakeupSleepOnDatalineConfigSet(FibexElement):
    """AUTOSAR EthernetWakeupSleepOnDatalineConfigSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ethernets: list[Any]
    def __init__(self) -> None:
        """Initialize EthernetWakeupSleepOnDatalineConfigSet."""
        super().__init__()
        self.ethernets: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetWakeupSleepOnDatalineConfigSet":
        """Deserialize XML element to EthernetWakeupSleepOnDatalineConfigSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetWakeupSleepOnDatalineConfigSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetWakeupSleepOnDatalineConfigSet, cls).deserialize(element)

        # Parse ethernets (list from container "ETHERNETS")
        obj.ethernets = []
        container = ARObject._find_child_element(element, "ETHERNETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ethernets.append(child_value)

        return obj



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
