"""ExecutionTimeConstraint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ExecutionTimeConstraint(TimingConstraint):
    """AUTOSAR ExecutionTimeConstraint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("component", None, False, False, any (SwComponent)),  # component
        ("executable_entity", None, False, False, ExecutableEntity),  # executableEntity
        ("execution_time", None, False, False, ExecutionTimeTypeEnum),  # executionTime
        ("maximum", None, False, False, MultidimensionalTime),  # maximum
        ("minimum", None, False, False, MultidimensionalTime),  # minimum
    ]

    def __init__(self) -> None:
        """Initialize ExecutionTimeConstraint."""
        super().__init__()
        self.component: Optional[Any] = None
        self.executable_entity: Optional[ExecutableEntity] = None
        self.execution_time: Optional[ExecutionTimeTypeEnum] = None
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ExecutionTimeConstraint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutionTimeConstraint":
        """Create ExecutionTimeConstraint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ExecutionTimeConstraint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ExecutionTimeConstraint since parent returns ARObject
        return cast("ExecutionTimeConstraint", obj)


class ExecutionTimeConstraintBuilder:
    """Builder for ExecutionTimeConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutionTimeConstraint = ExecutionTimeConstraint()

    def build(self) -> ExecutionTimeConstraint:
        """Build and return ExecutionTimeConstraint object.

        Returns:
            ExecutionTimeConstraint instance
        """
        # TODO: Add validation
        return self._obj
