"""SimulatedExecutionTime AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class SimulatedExecutionTime(ExecutionTime):
    """AUTOSAR SimulatedExecutionTime."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("maximum_execution_time", None, False, False, MultidimensionalTime),  # maximumExecutionTime
        ("minimum_execution_time", None, False, False, MultidimensionalTime),  # minimumExecutionTime
        ("nominal_execution_time", None, False, False, MultidimensionalTime),  # nominalExecutionTime
    ]

    def __init__(self) -> None:
        """Initialize SimulatedExecutionTime."""
        super().__init__()
        self.maximum_execution_time: Optional[MultidimensionalTime] = None
        self.minimum_execution_time: Optional[MultidimensionalTime] = None
        self.nominal_execution_time: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SimulatedExecutionTime to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SimulatedExecutionTime":
        """Create SimulatedExecutionTime from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SimulatedExecutionTime instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SimulatedExecutionTime since parent returns ARObject
        return cast("SimulatedExecutionTime", obj)


class SimulatedExecutionTimeBuilder:
    """Builder for SimulatedExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SimulatedExecutionTime = SimulatedExecutionTime()

    def build(self) -> SimulatedExecutionTime:
        """Build and return SimulatedExecutionTime object.

        Returns:
            SimulatedExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
