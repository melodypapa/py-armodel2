"""ExecutionOrderConstraint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)


class ExecutionOrderConstraint(TimingConstraint):
    """AUTOSAR ExecutionOrderConstraint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, CompositionSwComponentType),  # base
        ("execution_order", None, False, False, any (ExecutionOrder)),  # executionOrder
        ("ignore_order", None, True, False, None),  # ignoreOrder
        ("is_event", None, True, False, None),  # isEvent
        ("ordered_elements", None, False, True, any (EOCExecutableEntity)),  # orderedElements
        ("permit_multiple", None, True, False, None),  # permitMultiple
    ]

    def __init__(self) -> None:
        """Initialize ExecutionOrderConstraint."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.execution_order: Optional[Any] = None
        self.ignore_order: Optional[Boolean] = None
        self.is_event: Optional[Boolean] = None
        self.ordered_elements: list[Any] = []
        self.permit_multiple: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ExecutionOrderConstraint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutionOrderConstraint":
        """Create ExecutionOrderConstraint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ExecutionOrderConstraint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ExecutionOrderConstraint since parent returns ARObject
        return cast("ExecutionOrderConstraint", obj)


class ExecutionOrderConstraintBuilder:
    """Builder for ExecutionOrderConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutionOrderConstraint = ExecutionOrderConstraint()

    def build(self) -> ExecutionOrderConstraint:
        """Build and return ExecutionOrderConstraint object.

        Returns:
            ExecutionOrderConstraint instance
        """
        # TODO: Add validation
        return self._obj
