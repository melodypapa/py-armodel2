"""QueuedReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.receiver_com_spec import (
    ReceiverComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class QueuedReceiverComSpec(ReceiverComSpec):
    """AUTOSAR QueuedReceiverComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    queue_length: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize QueuedReceiverComSpec."""
        super().__init__()
        self.queue_length: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "QueuedReceiverComSpec":
        """Deserialize XML element to QueuedReceiverComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized QueuedReceiverComSpec object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse queue_length
        child = ARObject._find_child_element(element, "QUEUE-LENGTH")
        if child is not None:
            queue_length_value = child.text
            obj.queue_length = queue_length_value

        return obj



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
