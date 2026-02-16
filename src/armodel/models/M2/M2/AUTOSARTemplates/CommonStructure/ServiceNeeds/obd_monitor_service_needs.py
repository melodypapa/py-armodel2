"""ObdMonitorServiceNeeds AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)


class ObdMonitorServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdMonitorServiceNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "application_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationDataType,
        ),  # applicationData
        "event_needs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEventNeeds,
        ),  # eventNeeds
        "unit_and_scaling_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # unitAndScalingId
        "update_kind": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticMonitorUpdateKindEnum,
        ),  # updateKind
    }

    def __init__(self) -> None:
        """Initialize ObdMonitorServiceNeeds."""
        super().__init__()
        self.application_data: Optional[ApplicationDataType] = None
        self.event_needs: Optional[DiagnosticEventNeeds] = None
        self.unit_and_scaling_id: Optional[PositiveInteger] = None
        self.update_kind: Optional[DiagnosticMonitorUpdateKindEnum] = None


class ObdMonitorServiceNeedsBuilder:
    """Builder for ObdMonitorServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ObdMonitorServiceNeeds = ObdMonitorServiceNeeds()

    def build(self) -> ObdMonitorServiceNeeds:
        """Build and return ObdMonitorServiceNeeds object.

        Returns:
            ObdMonitorServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
