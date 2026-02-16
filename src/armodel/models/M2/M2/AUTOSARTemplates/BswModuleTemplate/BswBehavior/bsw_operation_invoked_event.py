"""BswOperationInvokedEvent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)


class BswOperationInvokedEvent(BswEvent):
    """AUTOSAR BswOperationInvokedEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "entry": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleClientServerEntry,
        ),  # entry
    }

    def __init__(self) -> None:
        """Initialize BswOperationInvokedEvent."""
        super().__init__()
        self.entry: Optional[BswModuleClientServerEntry] = None


class BswOperationInvokedEventBuilder:
    """Builder for BswOperationInvokedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswOperationInvokedEvent = BswOperationInvokedEvent()

    def build(self) -> BswOperationInvokedEvent:
        """Build and return BswOperationInvokedEvent object.

        Returns:
            BswOperationInvokedEvent instance
        """
        # TODO: Add validation
        return self._obj
