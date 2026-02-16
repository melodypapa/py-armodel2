"""IdsmTrafficLimitation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    PositiveInteger,
)


class IdsmTrafficLimitation(Identifiable):
    """AUTOSAR IdsmTrafficLimitation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max_bytes_in": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxBytesIn
        "time_interval": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeInterval
    }

    def __init__(self) -> None:
        """Initialize IdsmTrafficLimitation."""
        super().__init__()
        self.max_bytes_in: Optional[PositiveInteger] = None
        self.time_interval: Optional[Float] = None


class IdsmTrafficLimitationBuilder:
    """Builder for IdsmTrafficLimitation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmTrafficLimitation = IdsmTrafficLimitation()

    def build(self) -> IdsmTrafficLimitation:
        """Build and return IdsmTrafficLimitation object.

        Returns:
            IdsmTrafficLimitation instance
        """
        # TODO: Add validation
        return self._obj
