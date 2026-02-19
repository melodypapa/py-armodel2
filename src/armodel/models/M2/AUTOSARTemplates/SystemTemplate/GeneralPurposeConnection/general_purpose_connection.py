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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GeneralPurposeConnection, cls).deserialize(element)

        # Parse pdu_triggering_refs (list from container "PDU-TRIGGERINGS")
        obj.pdu_triggering_refs = []
        container = ARObject._find_child_element(element, "PDU-TRIGGERINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pdu_triggering_refs.append(child_value)

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
