"""FlexrayTpPduPool AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 596)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class FlexrayTpPduPool(Identifiable):
    """AUTOSAR FlexrayTpPduPool."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    n_pdus: list[NPdu]
    def __init__(self) -> None:
        """Initialize FlexrayTpPduPool."""
        super().__init__()
        self.n_pdus: list[NPdu] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpPduPool":
        """Deserialize XML element to FlexrayTpPduPool object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpPduPool object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse n_pdus (list)
        obj.n_pdus = []
        for child in ARObject._find_all_child_elements(element, "N-PDUS"):
            n_pdus_value = ARObject._deserialize_by_tag(child, "NPdu")
            obj.n_pdus.append(n_pdus_value)

        return obj



class FlexrayTpPduPoolBuilder:
    """Builder for FlexrayTpPduPool."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpPduPool = FlexrayTpPduPool()

    def build(self) -> FlexrayTpPduPool:
        """Build and return FlexrayTpPduPool object.

        Returns:
            FlexrayTpPduPool instance
        """
        # TODO: Add validation
        return self._obj
