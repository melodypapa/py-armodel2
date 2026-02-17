"""TransmissionModeCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)


class TransmissionModeCondition(ARObject):
    """AUTOSAR TransmissionModeCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_filter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataFilter,
        ),  # dataFilter
        "i_signal_in_i_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ISignalToIPduMapping,
        ),  # iSignalInIPdu
    }

    def __init__(self) -> None:
        """Initialize TransmissionModeCondition."""
        super().__init__()
        self.data_filter: Optional[DataFilter] = None
        self.i_signal_in_i_pdu: Optional[ISignalToIPduMapping] = None


class TransmissionModeConditionBuilder:
    """Builder for TransmissionModeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionModeCondition = TransmissionModeCondition()

    def build(self) -> TransmissionModeCondition:
        """Build and return TransmissionModeCondition object.

        Returns:
            TransmissionModeCondition instance
        """
        # TODO: Add validation
        return self._obj
