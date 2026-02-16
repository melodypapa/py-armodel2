"""TDEventOperation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class TDEventOperation(TDEventVfbPort):
    """AUTOSAR TDEventOperation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "operation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ClientServerOperation,
        ),  # operation
        "td_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TDEventOperationTypeEnum,
        ),  # tdEvent
    }

    def __init__(self) -> None:
        """Initialize TDEventOperation."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None
        self.td_event: Optional[TDEventOperationTypeEnum] = None


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
