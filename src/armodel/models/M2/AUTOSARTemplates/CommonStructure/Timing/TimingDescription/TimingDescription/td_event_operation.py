"""TDEventOperation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 55)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventOperationTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class TDEventOperation(TDEventVfbPort):
    """AUTOSAR TDEventOperation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation: Optional[ClientServerOperation]
    td_event: Optional[TDEventOperationTypeEnum]
    def __init__(self) -> None:
        """Initialize TDEventOperation."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None
        self.td_event: Optional[TDEventOperationTypeEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventOperation":
        """Deserialize XML element to TDEventOperation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventOperation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventOperation, cls).deserialize(element)

        # Parse operation
        child = ARObject._find_child_element(element, "OPERATION")
        if child is not None:
            operation_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.operation = operation_value

        # Parse td_event
        child = ARObject._find_child_element(element, "TD-EVENT")
        if child is not None:
            td_event_value = TDEventOperationTypeEnum.deserialize(child)
            obj.td_event = td_event_value

        return obj



class TDEventOperationBuilder:
    """Builder for TDEventOperation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventOperation = TDEventOperation()

    def build(self) -> TDEventOperation:
        """Build and return TDEventOperation object.

        Returns:
            TDEventOperation instance
        """
        # TODO: Add validation
        return self._obj
