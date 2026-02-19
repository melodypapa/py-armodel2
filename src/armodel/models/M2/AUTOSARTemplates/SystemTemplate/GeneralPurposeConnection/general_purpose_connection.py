"""GeneralPurposeConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 388)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GeneralPurposeConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class GeneralPurposeConnection(ARElement):
    """AUTOSAR GeneralPurposeConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    pdu_triggering_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize GeneralPurposeConnection."""
        super().__init__()
        self.pdu_triggering_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "GeneralPurposeConnection":
        """Deserialize XML element to GeneralPurposeConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GeneralPurposeConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse pdu_triggering_refs (list)
        obj.pdu_triggering_refs = []
        for child in ARObject._find_all_child_elements(element, "PDU-TRIGGERINGS"):
            pdu_triggering_refs_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.pdu_triggering_refs.append(pdu_triggering_refs_value)

        return obj



class GeneralPurposeConnectionBuilder:
    """Builder for GeneralPurposeConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GeneralPurposeConnection = GeneralPurposeConnection()

    def build(self) -> GeneralPurposeConnection:
        """Build and return GeneralPurposeConnection object.

        Returns:
            GeneralPurposeConnection instance
        """
        # TODO: Add validation
        return self._obj
