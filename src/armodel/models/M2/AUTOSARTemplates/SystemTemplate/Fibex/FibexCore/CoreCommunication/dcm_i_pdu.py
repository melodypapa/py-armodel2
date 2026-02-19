"""DcmIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 343)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    DiagPduType,
)


class DcmIPdu(IPdu):
    """AUTOSAR DcmIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diag_pdu_type: Optional[DiagPduType]
    def __init__(self) -> None:
        """Initialize DcmIPdu."""
        super().__init__()
        self.diag_pdu_type: Optional[DiagPduType] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DcmIPdu":
        """Deserialize XML element to DcmIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DcmIPdu object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse diag_pdu_type
        child = ARObject._find_child_element(element, "DIAG-PDU-TYPE")
        if child is not None:
            diag_pdu_type_value = child.text
            obj.diag_pdu_type = diag_pdu_type_value

        return obj



class DcmIPduBuilder:
    """Builder for DcmIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DcmIPdu = DcmIPdu()

    def build(self) -> DcmIPdu:
        """Build and return DcmIPdu object.

        Returns:
            DcmIPdu instance
        """
        # TODO: Add validation
        return self._obj
