"""AgeConstraint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class AgeConstraint(TimingConstraint):
    """AUTOSAR AgeConstraint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("maximum", None, False, False, MultidimensionalTime),  # maximum
        ("minimum", None, False, False, MultidimensionalTime),  # minimum
        ("scope", None, False, False, TimingDescriptionEvent),  # scope
    ]

    def __init__(self) -> None:
        """Initialize AgeConstraint."""
        super().__init__()
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None
        self.scope: Optional[TimingDescriptionEvent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AgeConstraint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AgeConstraint":
        """Create AgeConstraint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AgeConstraint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AgeConstraint since parent returns ARObject
        return cast("AgeConstraint", obj)


class AgeConstraintBuilder:
    """Builder for AgeConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AgeConstraint = AgeConstraint()

    def build(self) -> AgeConstraint:
        """Build and return AgeConstraint object.

        Returns:
            AgeConstraint instance
        """
        # TODO: Add validation
        return self._obj
