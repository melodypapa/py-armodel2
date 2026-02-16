"""BurstPatternEventTriggering AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class BurstPatternEventTriggering(EventTriggeringConstraint):
    """AUTOSAR BurstPatternEventTriggering."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_number_of", None, True, False, None),  # maxNumberOf
        ("minimum_inter", None, False, False, MultidimensionalTime),  # minimumInter
        ("min_number_of", None, True, False, None),  # minNumberOf
        ("pattern_jitter", None, False, False, MultidimensionalTime),  # patternJitter
        ("pattern_length", None, False, False, MultidimensionalTime),  # patternLength
        ("pattern_period", None, False, False, MultidimensionalTime),  # patternPeriod
    ]

    def __init__(self) -> None:
        """Initialize BurstPatternEventTriggering."""
        super().__init__()
        self.max_number_of: Optional[PositiveInteger] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.min_number_of: Optional[PositiveInteger] = None
        self.pattern_jitter: Optional[MultidimensionalTime] = None
        self.pattern_length: Optional[MultidimensionalTime] = None
        self.pattern_period: Optional[MultidimensionalTime] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BurstPatternEventTriggering to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BurstPatternEventTriggering":
        """Create BurstPatternEventTriggering from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BurstPatternEventTriggering instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BurstPatternEventTriggering since parent returns ARObject
        return cast("BurstPatternEventTriggering", obj)


class BurstPatternEventTriggeringBuilder:
    """Builder for BurstPatternEventTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BurstPatternEventTriggering = BurstPatternEventTriggering()

    def build(self) -> BurstPatternEventTriggering:
        """Build and return BurstPatternEventTriggering object.

        Returns:
            BurstPatternEventTriggering instance
        """
        # TODO: Add validation
        return self._obj
