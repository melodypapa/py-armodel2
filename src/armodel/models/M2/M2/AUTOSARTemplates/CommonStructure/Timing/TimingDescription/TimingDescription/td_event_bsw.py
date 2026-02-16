"""TDEventBsw AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
    BswModuleDescription,
)


class TDEventBsw(TimingDescriptionEvent):
    """AUTOSAR TDEventBsw."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bsw_module_description": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleDescription,
        ),  # bswModuleDescription
    }

    def __init__(self) -> None:
        """Initialize TDEventBsw."""
        super().__init__()
        self.bsw_module_description: Optional[BswModuleDescription] = None


class TDEventBswBuilder:
    """Builder for TDEventBsw."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBsw = TDEventBsw()

    def build(self) -> TDEventBsw:
        """Build and return TDEventBsw object.

        Returns:
            TDEventBsw instance
        """
        # TODO: Add validation
        return self._obj
