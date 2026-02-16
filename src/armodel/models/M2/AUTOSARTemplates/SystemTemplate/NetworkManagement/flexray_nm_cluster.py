"""FlexrayNmCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)


class FlexrayNmCluster(NmCluster):
    """AUTOSAR FlexrayNmCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("nm_car_wake_up", None, True, False, None),  # nmCarWakeUp
        ("nm_data_cycle", None, True, False, None),  # nmDataCycle
        ("nm_main", None, True, False, None),  # nmMain
        ("nm_remote", None, True, False, None),  # nmRemote
        ("nm_repeat", None, True, False, None),  # nmRepeat
        ("nm_repetition", None, True, False, None),  # nmRepetition
        ("nm_voting_cycle", None, True, False, None),  # nmVotingCycle
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayNmCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayNmCluster":
        """Create FlexrayNmCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayNmCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayNmCluster since parent returns ARObject
        return cast("FlexrayNmCluster", obj)


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
