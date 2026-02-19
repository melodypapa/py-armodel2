"""IEEE1722TpAcfLinPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 667)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class IEEE1722TpAcfLinPart(IEEE1722TpAcfBusPart):
    """AUTOSAR IEEE1722TpAcfLinPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lin_identifier: Optional[PositiveInteger]
    sdu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfLinPart."""
        super().__init__()
        self.lin_identifier: Optional[PositiveInteger] = None
        self.sdu_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfLinPart":
        """Deserialize XML element to IEEE1722TpAcfLinPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfLinPart object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse lin_identifier
        child = ARObject._find_child_element(element, "LIN-IDENTIFIER")
        if child is not None:
            lin_identifier_value = child.text
            obj.lin_identifier = lin_identifier_value

        # Parse sdu_ref
        child = ARObject._find_child_element(element, "SDU")
        if child is not None:
            sdu_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.sdu_ref = sdu_ref_value

        return obj



class IEEE1722TpAcfLinPartBuilder:
    """Builder for IEEE1722TpAcfLinPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfLinPart = IEEE1722TpAcfLinPart()

    def build(self) -> IEEE1722TpAcfLinPart:
        """Build and return IEEE1722TpAcfLinPart object.

        Returns:
            IEEE1722TpAcfLinPart instance
        """
        # TODO: Add validation
        return self._obj
