"""ObdMonitorServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 797)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticMonitorUpdateKindEnum,
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_data: Optional[ApplicationDataType]
    event_needs: Optional[DiagnosticEventNeeds]
    unit_and_scaling_id: Optional[PositiveInteger]
    update_kind: Optional[DiagnosticMonitorUpdateKindEnum]
    def __init__(self) -> None:
        """Initialize ObdMonitorServiceNeeds."""
        super().__init__()
        self.application_data: Optional[ApplicationDataType] = None
        self.event_needs: Optional[DiagnosticEventNeeds] = None
        self.unit_and_scaling_id: Optional[PositiveInteger] = None
        self.update_kind: Optional[DiagnosticMonitorUpdateKindEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdMonitorServiceNeeds":
        """Deserialize XML element to ObdMonitorServiceNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ObdMonitorServiceNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ObdMonitorServiceNeeds, cls).deserialize(element)

        # Parse application_data
        child = ARObject._find_child_element(element, "APPLICATION-DATA")
        if child is not None:
            application_data_value = ARObject._deserialize_by_tag(child, "ApplicationDataType")
            obj.application_data = application_data_value

        # Parse event_needs
        child = ARObject._find_child_element(element, "EVENT-NEEDS")
        if child is not None:
            event_needs_value = ARObject._deserialize_by_tag(child, "DiagnosticEventNeeds")
            obj.event_needs = event_needs_value

        # Parse unit_and_scaling_id
        child = ARObject._find_child_element(element, "UNIT-AND-SCALING-ID")
        if child is not None:
            unit_and_scaling_id_value = child.text
            obj.unit_and_scaling_id = unit_and_scaling_id_value

        # Parse update_kind
        child = ARObject._find_child_element(element, "UPDATE-KIND")
        if child is not None:
            update_kind_value = DiagnosticMonitorUpdateKindEnum.deserialize(child)
            obj.update_kind = update_kind_value

        return obj



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
