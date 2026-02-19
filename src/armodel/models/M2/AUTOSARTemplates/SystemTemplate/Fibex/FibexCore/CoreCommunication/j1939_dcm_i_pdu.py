"""J1939DcmIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 321)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class J1939DcmIPdu(IPdu):
    """AUTOSAR J1939DcmIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic: Optional[PositiveInteger]
    message_type: Any
    def __init__(self) -> None:
        """Initialize J1939DcmIPdu."""
        super().__init__()
        self.diagnostic: Optional[PositiveInteger] = None
        self.message_type: Any = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939DcmIPdu":
        """Deserialize XML element to J1939DcmIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939DcmIPdu object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse diagnostic
        child = ARObject._find_child_element(element, "DIAGNOSTIC")
        if child is not None:
            diagnostic_value = child.text
            obj.diagnostic = diagnostic_value

        # Parse message_type
        child = ARObject._find_child_element(element, "MESSAGE-TYPE")
        if child is not None:
            message_type_value = child.text
            obj.message_type = message_type_value

        return obj



class J1939DcmIPduBuilder:
    """Builder for J1939DcmIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939DcmIPdu = J1939DcmIPdu()

    def build(self) -> J1939DcmIPdu:
        """Build and return J1939DcmIPdu object.

        Returns:
            J1939DcmIPdu instance
        """
        # TODO: Add validation
        return self._obj
