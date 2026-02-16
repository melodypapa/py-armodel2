"""ConfidenceInterval AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ConfidenceInterval(ARObject):
    """AUTOSAR ConfidenceInterval."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("lower_bound", None, False, False, MultidimensionalTime),  # lowerBound
        ("propability", None, True, False, None),  # propability
        ("upper_bound", None, False, False, MultidimensionalTime),  # upperBound
    ]

    def __init__(self) -> None:
        """Initialize ConfidenceInterval."""
        super().__init__()
        self.lower_bound: Optional[MultidimensionalTime] = None
        self.propability: Optional[Float] = None
        self.upper_bound: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConfidenceInterval to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConfidenceInterval":
        """Create ConfidenceInterval from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConfidenceInterval instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConfidenceInterval since parent returns ARObject
        return cast("ConfidenceInterval", obj)


class ConfidenceIntervalBuilder:
    """Builder for ConfidenceInterval."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConfidenceInterval = ConfidenceInterval()

    def build(self) -> ConfidenceInterval:
        """Build and return ConfidenceInterval object.

        Returns:
            ConfidenceInterval instance
        """
        # TODO: Add validation
        return self._obj
