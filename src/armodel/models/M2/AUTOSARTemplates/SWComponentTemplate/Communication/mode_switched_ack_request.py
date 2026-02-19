"""ModeSwitchedAckRequest AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class ModeSwitchedAckRequest(ARObject):
    """AUTOSAR ModeSwitchedAckRequest."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize ModeSwitchedAckRequest."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchedAckRequest":
        """Deserialize XML element to ModeSwitchedAckRequest object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchedAckRequest object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse timeout
        child = ARObject._find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = child.text
            obj.timeout = timeout_value

        return obj



class ModeSwitchedAckRequestBuilder:
    """Builder for ModeSwitchedAckRequest."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchedAckRequest = ModeSwitchedAckRequest()

    def build(self) -> ModeSwitchedAckRequest:
        """Build and return ModeSwitchedAckRequest object.

        Returns:
            ModeSwitchedAckRequest instance
        """
        # TODO: Add validation
        return self._obj
