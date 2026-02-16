"""AgeConstraint AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "maximum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # maximum
        "minimum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # minimum
        "scope": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingDescriptionEvent,
        ),  # scope
    }

    def __init__(self) -> None:
        """Initialize AgeConstraint."""
        super().__init__()
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None
        self.scope: Optional[TimingDescriptionEvent] = None


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
