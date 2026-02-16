"""TimingDescriptionEventChain AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class TimingDescriptionEventChain(TimingDescription):
    """AUTOSAR TimingDescriptionEventChain."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "is_pipelining": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isPipelining
        "response": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingDescriptionEvent,
        ),  # response
        "segments": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TimingDescriptionEvent,
        ),  # segments
        "stimulus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingDescriptionEvent,
        ),  # stimulus
    }

    def __init__(self) -> None:
        """Initialize TimingDescriptionEventChain."""
        super().__init__()
        self.is_pipelining: Optional[Boolean] = None
        self.response: Optional[TimingDescriptionEvent] = None
        self.segments: list[TimingDescriptionEvent] = []
        self.stimulus: Optional[TimingDescriptionEvent] = None


class TimingDescriptionEventChainBuilder:
    """Builder for TimingDescriptionEventChain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingDescriptionEventChain = TimingDescriptionEventChain()

    def build(self) -> TimingDescriptionEventChain:
        """Build and return TimingDescriptionEventChain object.

        Returns:
            TimingDescriptionEventChain instance
        """
        # TODO: Add validation
        return self._obj
