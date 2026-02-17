"""QueuedReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.receiver_com_spec import (
    ReceiverComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class QueuedReceiverComSpec(ReceiverComSpec):
    """AUTOSAR QueuedReceiverComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "queue_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # queueLength
    }

    def __init__(self) -> None:
        """Initialize QueuedReceiverComSpec."""
        super().__init__()
        self.queue_length: Optional[PositiveInteger] = None


class QueuedReceiverComSpecBuilder:
    """Builder for QueuedReceiverComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: QueuedReceiverComSpec = QueuedReceiverComSpec()

    def build(self) -> QueuedReceiverComSpec:
        """Build and return QueuedReceiverComSpec object.

        Returns:
            QueuedReceiverComSpec instance
        """
        # TODO: Add validation
        return self._obj
