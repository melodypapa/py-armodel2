"""QueuedSenderComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 179)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.sender_com_spec import (
    SenderComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class QueuedSenderComSpec(SenderComSpec):
    """AUTOSAR QueuedSenderComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize QueuedSenderComSpec."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "QueuedSenderComSpec":
        """Deserialize XML element to QueuedSenderComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized QueuedSenderComSpec object
        """
        # Delegate to parent class to handle inherited attributes
        return super(QueuedSenderComSpec, cls).deserialize(element)



class QueuedSenderComSpecBuilder:
    """Builder for QueuedSenderComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: QueuedSenderComSpec = QueuedSenderComSpec()

    def build(self) -> QueuedSenderComSpec:
        """Build and return QueuedSenderComSpec object.

        Returns:
            QueuedSenderComSpec instance
        """
        # TODO: Add validation
        return self._obj
