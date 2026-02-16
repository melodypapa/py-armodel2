"""ExecutableEntity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects.sw_addr_method import (
    SwAddrMethod,
)


class ExecutableEntity(Identifiable):
    """AUTOSAR ExecutableEntity."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("activations", None, False, True, ExecutableEntity),  # activations
        ("can_enters", None, False, True, ExclusiveArea),  # canEnters
        ("exclusive_area_nestings", None, False, True, ExclusiveAreaNestingOrder),  # exclusiveAreaNestings
        ("minimum_start", None, True, False, None),  # minimumStart
        ("reentrancy_level_enum", None, False, False, ReentrancyLevelEnum),  # reentrancyLevelEnum
        ("runs_insides", None, False, True, ExclusiveArea),  # runsInsides
        ("sw_addr_method", None, False, False, SwAddrMethod),  # swAddrMethod
    ]

    def __init__(self) -> None:
        """Initialize ExecutableEntity."""
        super().__init__()
        self.activations: list[ExecutableEntity] = []
        self.can_enters: list[ExclusiveArea] = []
        self.exclusive_area_nestings: list[ExclusiveAreaNestingOrder] = []
        self.minimum_start: Optional[TimeValue] = None
        self.reentrancy_level_enum: Optional[ReentrancyLevelEnum] = None
        self.runs_insides: list[ExclusiveArea] = []
        self.sw_addr_method: Optional[SwAddrMethod] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ExecutableEntity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutableEntity":
        """Create ExecutableEntity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ExecutableEntity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ExecutableEntity since parent returns ARObject
        return cast("ExecutableEntity", obj)


class ExecutableEntityBuilder:
    """Builder for ExecutableEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutableEntity = ExecutableEntity()

    def build(self) -> ExecutableEntity:
        """Build and return ExecutableEntity object.

        Returns:
            ExecutableEntity instance
        """
        # TODO: Add validation
        return self._obj
