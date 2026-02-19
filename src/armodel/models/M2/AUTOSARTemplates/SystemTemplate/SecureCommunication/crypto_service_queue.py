"""CryptoServiceQueue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 381)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoServiceQueue(ARElement):
    """AUTOSAR CryptoServiceQueue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    queue_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CryptoServiceQueue."""
        super().__init__()
        self.queue_size: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceQueue":
        """Deserialize XML element to CryptoServiceQueue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoServiceQueue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse queue_size
        child = ARObject._find_child_element(element, "QUEUE-SIZE")
        if child is not None:
            queue_size_value = child.text
            obj.queue_size = queue_size_value

        return obj



class CryptoServiceQueueBuilder:
    """Builder for CryptoServiceQueue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceQueue = CryptoServiceQueue()

    def build(self) -> CryptoServiceQueue:
        """Build and return CryptoServiceQueue object.

        Returns:
            CryptoServiceQueue instance
        """
        # TODO: Add validation
        return self._obj
