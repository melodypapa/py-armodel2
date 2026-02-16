"""ExecutableEntityActivationReason AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class ExecutableEntityActivationReason(ImplementationProps):
    """AUTOSAR ExecutableEntityActivationReason."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bit_position", None, True, False, None),  # bitPosition
    ]

    def __init__(self) -> None:
        """Initialize ExecutableEntityActivationReason."""
        super().__init__()
        self.bit_position: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ExecutableEntityActivationReason to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutableEntityActivationReason":
        """Create ExecutableEntityActivationReason from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ExecutableEntityActivationReason instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ExecutableEntityActivationReason since parent returns ARObject
        return cast("ExecutableEntityActivationReason", obj)


class ExecutableEntityActivationReasonBuilder:
    """Builder for ExecutableEntityActivationReason."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutableEntityActivationReason = ExecutableEntityActivationReason()

    def build(self) -> ExecutableEntityActivationReason:
        """Build and return ExecutableEntityActivationReason object.

        Returns:
            ExecutableEntityActivationReason instance
        """
        # TODO: Add validation
        return self._obj
