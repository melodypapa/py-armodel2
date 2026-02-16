"""ObdRatioServiceNeeds AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class ObdRatioServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdRatioServiceNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "connection_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ObdRatioConnectionKindEnum,
        ),  # connectionType
        "rate_based_monitored_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEventNeeds,
        ),  # rateBasedMonitoredEvent
        "used_fid": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FunctionInhibitionNeeds,
        ),  # usedFid
    }

    def __init__(self) -> None:
        """Initialize ObdRatioServiceNeeds."""
        super().__init__()
        self.connection_type: Optional[ObdRatioConnectionKindEnum] = None
        self.rate_based_monitored_event: Optional[DiagnosticEventNeeds] = None
        self.used_fid: Optional[FunctionInhibitionNeeds] = None


class ObdRatioServiceNeedsBuilder:
    """Builder for ObdRatioServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ObdRatioServiceNeeds = ObdRatioServiceNeeds()

    def build(self) -> ObdRatioServiceNeeds:
        """Build and return ObdRatioServiceNeeds object.

        Returns:
            ObdRatioServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
