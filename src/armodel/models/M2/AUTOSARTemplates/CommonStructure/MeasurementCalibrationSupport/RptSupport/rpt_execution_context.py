"""RptExecutionContext AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class RptExecutionContext(Identifiable):
    """AUTOSAR RptExecutionContext."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize RptExecutionContext."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RptExecutionContext to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptExecutionContext":
        """Create RptExecutionContext from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RptExecutionContext instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RptExecutionContext since parent returns ARObject
        return cast("RptExecutionContext", obj)


class RptExecutionContextBuilder:
    """Builder for RptExecutionContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptExecutionContext = RptExecutionContext()

    def build(self) -> RptExecutionContext:
        """Build and return RptExecutionContext object.

        Returns:
            RptExecutionContext instance
        """
        # TODO: Add validation
        return self._obj
