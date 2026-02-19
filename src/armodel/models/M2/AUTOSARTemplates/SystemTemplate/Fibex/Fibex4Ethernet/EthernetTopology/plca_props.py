"""PlcaProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 169)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class PlcaProps(ARObject):
    """AUTOSAR PlcaProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    plca_local_node: Optional[PositiveInteger]
    plca_max_burst: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize PlcaProps."""
        super().__init__()
        self.plca_local_node: Optional[PositiveInteger] = None
        self.plca_max_burst: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PlcaProps":
        """Deserialize XML element to PlcaProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PlcaProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse plca_local_node
        child = ARObject._find_child_element(element, "PLCA-LOCAL-NODE")
        if child is not None:
            plca_local_node_value = child.text
            obj.plca_local_node = plca_local_node_value

        # Parse plca_max_burst
        child = ARObject._find_child_element(element, "PLCA-MAX-BURST")
        if child is not None:
            plca_max_burst_value = child.text
            obj.plca_max_burst = plca_max_burst_value

        return obj



class PlcaPropsBuilder:
    """Builder for PlcaProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PlcaProps = PlcaProps()

    def build(self) -> PlcaProps:
        """Build and return PlcaProps object.

        Returns:
            PlcaProps instance
        """
        # TODO: Add validation
        return self._obj
