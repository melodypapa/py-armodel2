"""CouplingPortAsynchronousTrafficShaper AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2012)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_asynchronous_traffic_shaper_group_entry import (
    SwitchAsynchronousTrafficShaperGroupEntry,
)


class CouplingPortAsynchronousTrafficShaper(Identifiable):
    """AUTOSAR CouplingPortAsynchronousTrafficShaper."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    committed_burst: Optional[PositiveInteger]
    committed: Optional[PositiveInteger]
    traffic_shaper: Optional[SwitchAsynchronousTrafficShaperGroupEntry]
    def __init__(self) -> None:
        """Initialize CouplingPortAsynchronousTrafficShaper."""
        super().__init__()
        self.committed_burst: Optional[PositiveInteger] = None
        self.committed: Optional[PositiveInteger] = None
        self.traffic_shaper: Optional[SwitchAsynchronousTrafficShaperGroupEntry] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortAsynchronousTrafficShaper":
        """Deserialize XML element to CouplingPortAsynchronousTrafficShaper object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortAsynchronousTrafficShaper object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortAsynchronousTrafficShaper, cls).deserialize(element)

        # Parse committed_burst
        child = ARObject._find_child_element(element, "COMMITTED-BURST")
        if child is not None:
            committed_burst_value = child.text
            obj.committed_burst = committed_burst_value

        # Parse committed
        child = ARObject._find_child_element(element, "COMMITTED")
        if child is not None:
            committed_value = child.text
            obj.committed = committed_value

        # Parse traffic_shaper
        child = ARObject._find_child_element(element, "TRAFFIC-SHAPER")
        if child is not None:
            traffic_shaper_value = ARObject._deserialize_by_tag(child, "SwitchAsynchronousTrafficShaperGroupEntry")
            obj.traffic_shaper = traffic_shaper_value

        return obj



class CouplingPortAsynchronousTrafficShaperBuilder:
    """Builder for CouplingPortAsynchronousTrafficShaper."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortAsynchronousTrafficShaper = CouplingPortAsynchronousTrafficShaper()

    def build(self) -> CouplingPortAsynchronousTrafficShaper:
        """Build and return CouplingPortAsynchronousTrafficShaper object.

        Returns:
            CouplingPortAsynchronousTrafficShaper instance
        """
        # TODO: Add validation
        return self._obj
