"""ObdRatioServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 795)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ObdRatioConnectionKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class ObdRatioServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdRatioServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connection_type: Optional[ObdRatioConnectionKindEnum]
    rate_based_monitored_event: Optional[DiagnosticEventNeeds]
    used_fid: Optional[FunctionInhibitionNeeds]
    def __init__(self) -> None:
        """Initialize ObdRatioServiceNeeds."""
        super().__init__()
        self.connection_type: Optional[ObdRatioConnectionKindEnum] = None
        self.rate_based_monitored_event: Optional[DiagnosticEventNeeds] = None
        self.used_fid: Optional[FunctionInhibitionNeeds] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdRatioServiceNeeds":
        """Deserialize XML element to ObdRatioServiceNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ObdRatioServiceNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ObdRatioServiceNeeds, cls).deserialize(element)

        # Parse connection_type
        child = ARObject._find_child_element(element, "CONNECTION-TYPE")
        if child is not None:
            connection_type_value = ObdRatioConnectionKindEnum.deserialize(child)
            obj.connection_type = connection_type_value

        # Parse rate_based_monitored_event
        child = ARObject._find_child_element(element, "RATE-BASED-MONITORED-EVENT")
        if child is not None:
            rate_based_monitored_event_value = ARObject._deserialize_by_tag(child, "DiagnosticEventNeeds")
            obj.rate_based_monitored_event = rate_based_monitored_event_value

        # Parse used_fid
        child = ARObject._find_child_element(element, "USED-FID")
        if child is not None:
            used_fid_value = ARObject._deserialize_by_tag(child, "FunctionInhibitionNeeds")
            obj.used_fid = used_fid_value

        return obj



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
