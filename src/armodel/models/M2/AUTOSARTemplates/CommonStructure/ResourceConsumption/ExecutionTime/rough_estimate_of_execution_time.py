"""RoughEstimateOfExecutionTime AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class RoughEstimateOfExecutionTime(ExecutionTime):
    """AUTOSAR RoughEstimateOfExecutionTime."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("additional", None, True, False, None),  # additional
        ("estimated_execution_time", None, False, False, MultidimensionalTime),  # estimatedExecutionTime
    ]

    def __init__(self) -> None:
        """Initialize RoughEstimateOfExecutionTime."""
        super().__init__()
        self.additional: Optional[String] = None
        self.estimated_execution_time: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RoughEstimateOfExecutionTime to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoughEstimateOfExecutionTime":
        """Create RoughEstimateOfExecutionTime from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RoughEstimateOfExecutionTime instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RoughEstimateOfExecutionTime since parent returns ARObject
        return cast("RoughEstimateOfExecutionTime", obj)


class RoughEstimateOfExecutionTimeBuilder:
    """Builder for RoughEstimateOfExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoughEstimateOfExecutionTime = RoughEstimateOfExecutionTime()

    def build(self) -> RoughEstimateOfExecutionTime:
        """Build and return RoughEstimateOfExecutionTime object.

        Returns:
            RoughEstimateOfExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
