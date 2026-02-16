"""DdsLatencyBudget AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsLatencyBudget(ARObject):
    """AUTOSAR DdsLatencyBudget."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("latency_budget", None, True, False, None),  # latencyBudget
    ]

    def __init__(self) -> None:
        """Initialize DdsLatencyBudget."""
        super().__init__()
        self.latency_budget: Optional[Float] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsLatencyBudget to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsLatencyBudget":
        """Create DdsLatencyBudget from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsLatencyBudget instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsLatencyBudget since parent returns ARObject
        return cast("DdsLatencyBudget", obj)


class DdsLatencyBudgetBuilder:
    """Builder for DdsLatencyBudget."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsLatencyBudget = DdsLatencyBudget()

    def build(self) -> DdsLatencyBudget:
        """Build and return DdsLatencyBudget object.

        Returns:
            DdsLatencyBudget instance
        """
        # TODO: Add validation
        return self._obj
