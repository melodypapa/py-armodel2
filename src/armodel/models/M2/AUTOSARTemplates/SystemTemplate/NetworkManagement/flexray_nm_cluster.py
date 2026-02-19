"""FlexrayNmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 678)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)


class FlexrayNmCluster(NmCluster):
    """AUTOSAR FlexrayNmCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nm_car_wake_up: Optional[Boolean]
    nm_data_cycle: Optional[Integer]
    nm_main: Optional[TimeValue]
    nm_remote: Optional[TimeValue]
    nm_repeat: Optional[TimeValue]
    nm_repetition: Optional[Integer]
    nm_voting_cycle: Optional[Integer]
    def __init__(self) -> None:
        """Initialize FlexrayNmCluster."""
        super().__init__()
        self.nm_car_wake_up: Optional[Boolean] = None
        self.nm_data_cycle: Optional[Integer] = None
        self.nm_main: Optional[TimeValue] = None
        self.nm_remote: Optional[TimeValue] = None
        self.nm_repeat: Optional[TimeValue] = None
        self.nm_repetition: Optional[Integer] = None
        self.nm_voting_cycle: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayNmCluster":
        """Deserialize XML element to FlexrayNmCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayNmCluster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse nm_car_wake_up
        child = ARObject._find_child_element(element, "NM-CAR-WAKE-UP")
        if child is not None:
            nm_car_wake_up_value = child.text
            obj.nm_car_wake_up = nm_car_wake_up_value

        # Parse nm_data_cycle
        child = ARObject._find_child_element(element, "NM-DATA-CYCLE")
        if child is not None:
            nm_data_cycle_value = child.text
            obj.nm_data_cycle = nm_data_cycle_value

        # Parse nm_main
        child = ARObject._find_child_element(element, "NM-MAIN")
        if child is not None:
            nm_main_value = child.text
            obj.nm_main = nm_main_value

        # Parse nm_remote
        child = ARObject._find_child_element(element, "NM-REMOTE")
        if child is not None:
            nm_remote_value = child.text
            obj.nm_remote = nm_remote_value

        # Parse nm_repeat
        child = ARObject._find_child_element(element, "NM-REPEAT")
        if child is not None:
            nm_repeat_value = child.text
            obj.nm_repeat = nm_repeat_value

        # Parse nm_repetition
        child = ARObject._find_child_element(element, "NM-REPETITION")
        if child is not None:
            nm_repetition_value = child.text
            obj.nm_repetition = nm_repetition_value

        # Parse nm_voting_cycle
        child = ARObject._find_child_element(element, "NM-VOTING-CYCLE")
        if child is not None:
            nm_voting_cycle_value = child.text
            obj.nm_voting_cycle = nm_voting_cycle_value

        return obj



class FlexrayNmClusterBuilder:
    """Builder for FlexrayNmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayNmCluster = FlexrayNmCluster()

    def build(self) -> FlexrayNmCluster:
        """Build and return FlexrayNmCluster object.

        Returns:
            FlexrayNmCluster instance
        """
        # TODO: Add validation
        return self._obj
