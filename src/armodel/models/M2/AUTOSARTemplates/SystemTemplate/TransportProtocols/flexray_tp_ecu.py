"""FlexrayTpEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 596)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class FlexrayTpEcu(ARObject):
    """AUTOSAR FlexrayTpEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cancellation: Optional[Boolean]
    cycle_time_main: Optional[TimeValue]
    ecu_instance: Optional[EcuInstance]
    full_duplex: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize FlexrayTpEcu."""
        super().__init__()
        self.cancellation: Optional[Boolean] = None
        self.cycle_time_main: Optional[TimeValue] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.full_duplex: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpEcu":
        """Deserialize XML element to FlexrayTpEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpEcu object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse cancellation
        child = ARObject._find_child_element(element, "CANCELLATION")
        if child is not None:
            cancellation_value = child.text
            obj.cancellation = cancellation_value

        # Parse cycle_time_main
        child = ARObject._find_child_element(element, "CYCLE-TIME-MAIN")
        if child is not None:
            cycle_time_main_value = child.text
            obj.cycle_time_main = cycle_time_main_value

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

        # Parse full_duplex
        child = ARObject._find_child_element(element, "FULL-DUPLEX")
        if child is not None:
            full_duplex_value = child.text
            obj.full_duplex = full_duplex_value

        return obj



class FlexrayTpEcuBuilder:
    """Builder for FlexrayTpEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpEcu = FlexrayTpEcu()

    def build(self) -> FlexrayTpEcu:
        """Build and return FlexrayTpEcu object.

        Returns:
            FlexrayTpEcu instance
        """
        # TODO: Add validation
        return self._obj
