"""NmPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 302)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)


class NmPdu(Pdu):
    """AUTOSAR NmPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_signal_to_i_pdu_refs: list[ARRef]
    nm_data: Optional[Boolean]
    nm_vote_information: Optional[Boolean]
    unused_bit: Optional[Integer]
    def __init__(self) -> None:
        """Initialize NmPdu."""
        super().__init__()
        self.i_signal_to_i_pdu_refs: list[ARRef] = []
        self.nm_data: Optional[Boolean] = None
        self.nm_vote_information: Optional[Boolean] = None
        self.unused_bit: Optional[Integer] = None


class NmPduBuilder:
    """Builder for NmPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmPdu = NmPdu()

    def build(self) -> NmPdu:
        """Build and return NmPdu object.

        Returns:
            NmPdu instance
        """
        # TODO: Add validation
        return self._obj
