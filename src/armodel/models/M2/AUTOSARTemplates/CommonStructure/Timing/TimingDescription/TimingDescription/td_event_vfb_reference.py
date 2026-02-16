"""TDEventVfbReference AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
    TDEventVfb,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
    TDEventVfb,
)


class TDEventVfbReference(TDEventVfb):
    """AUTOSAR TDEventVfbReference."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "referenced_td_event_vfb": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TDEventVfb,
        ),  # referencedTDEventVfb
    }

    def __init__(self) -> None:
        """Initialize TDEventVfbReference."""
        super().__init__()
        self.referenced_td_event_vfb: Optional[TDEventVfb] = None


class TDEventVfbReferenceBuilder:
    """Builder for TDEventVfbReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfbReference = TDEventVfbReference()

    def build(self) -> TDEventVfbReference:
        """Build and return TDEventVfbReference object.

        Returns:
            TDEventVfbReference instance
        """
        # TODO: Add validation
        return self._obj
