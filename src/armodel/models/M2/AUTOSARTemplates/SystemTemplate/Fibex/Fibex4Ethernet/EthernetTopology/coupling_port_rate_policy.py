"""CouplingPortRatePolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class CouplingPortRatePolicy(ARObject):
    """AUTOSAR CouplingPortRatePolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_length: Optional[PositiveInteger]
    policy_action: Optional[CouplingPortRatePolicy]
    priority: Optional[PositiveInteger]
    time_interval: Optional[TimeValue]
    v_lans: list[Any]
    def __init__(self) -> None:
        """Initialize CouplingPortRatePolicy."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.policy_action: Optional[CouplingPortRatePolicy] = None
        self.priority: Optional[PositiveInteger] = None
        self.time_interval: Optional[TimeValue] = None
        self.v_lans: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortRatePolicy":
        """Deserialize XML element to CouplingPortRatePolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortRatePolicy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_length
        child = ARObject._find_child_element(element, "DATA-LENGTH")
        if child is not None:
            data_length_value = child.text
            obj.data_length = data_length_value

        # Parse policy_action
        child = ARObject._find_child_element(element, "POLICY-ACTION")
        if child is not None:
            policy_action_value = ARObject._deserialize_by_tag(child, "CouplingPortRatePolicy")
            obj.policy_action = policy_action_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse time_interval
        child = ARObject._find_child_element(element, "TIME-INTERVAL")
        if child is not None:
            time_interval_value = child.text
            obj.time_interval = time_interval_value

        # Parse v_lans (list from container "V-LANS")
        obj.v_lans = []
        container = ARObject._find_child_element(element, "V-LANS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.v_lans.append(child_value)

        return obj



class CouplingPortRatePolicyBuilder:
    """Builder for CouplingPortRatePolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortRatePolicy = CouplingPortRatePolicy()

    def build(self) -> CouplingPortRatePolicy:
        """Build and return CouplingPortRatePolicy object.

        Returns:
            CouplingPortRatePolicy instance
        """
        # TODO: Add validation
        return self._obj
