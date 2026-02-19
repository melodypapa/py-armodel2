"""SwitchFlowMeteringEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 143)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    FlowMeteringColorModeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class SwitchFlowMeteringEntry(Identifiable):
    """AUTOSAR SwitchFlowMeteringEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    color_mode: Optional[FlowMeteringColorModeEnum]
    committed_burst: Optional[PositiveInteger]
    committed: Optional[PositiveInteger]
    coupling_flag: Optional[Boolean]
    excess_burst: Optional[PositiveInteger]
    excess: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SwitchFlowMeteringEntry."""
        super().__init__()
        self.color_mode: Optional[FlowMeteringColorModeEnum] = None
        self.committed_burst: Optional[PositiveInteger] = None
        self.committed: Optional[PositiveInteger] = None
        self.coupling_flag: Optional[Boolean] = None
        self.excess_burst: Optional[PositiveInteger] = None
        self.excess: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchFlowMeteringEntry":
        """Deserialize XML element to SwitchFlowMeteringEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchFlowMeteringEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchFlowMeteringEntry, cls).deserialize(element)

        # Parse color_mode
        child = ARObject._find_child_element(element, "COLOR-MODE")
        if child is not None:
            color_mode_value = FlowMeteringColorModeEnum.deserialize(child)
            obj.color_mode = color_mode_value

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

        # Parse coupling_flag
        child = ARObject._find_child_element(element, "COUPLING-FLAG")
        if child is not None:
            coupling_flag_value = child.text
            obj.coupling_flag = coupling_flag_value

        # Parse excess_burst
        child = ARObject._find_child_element(element, "EXCESS-BURST")
        if child is not None:
            excess_burst_value = child.text
            obj.excess_burst = excess_burst_value

        # Parse excess
        child = ARObject._find_child_element(element, "EXCESS")
        if child is not None:
            excess_value = child.text
            obj.excess = excess_value

        return obj



class SwitchFlowMeteringEntryBuilder:
    """Builder for SwitchFlowMeteringEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchFlowMeteringEntry = SwitchFlowMeteringEntry()

    def build(self) -> SwitchFlowMeteringEntry:
        """Build and return SwitchFlowMeteringEntry object.

        Returns:
            SwitchFlowMeteringEntry instance
        """
        # TODO: Add validation
        return self._obj
