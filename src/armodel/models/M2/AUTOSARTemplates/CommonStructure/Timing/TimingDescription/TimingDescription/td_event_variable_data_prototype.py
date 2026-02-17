"""TDEventVariableDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class TDEventVariableDataPrototype(TDEventVfbPort):
    """AUTOSAR TDEventVariableDataPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # dataElement
        "td_event_variable_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (TDEventVariableData),
        ),  # tdEventVariableType
    }

    def __init__(self) -> None:
        """Initialize TDEventVariableDataPrototype."""
        super().__init__()
        self.data_element: Optional[VariableDataPrototype] = None
        self.td_event_variable_type: Optional[Any] = None


class TDEventVariableDataPrototypeBuilder:
    """Builder for TDEventVariableDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVariableDataPrototype = TDEventVariableDataPrototype()

    def build(self) -> TDEventVariableDataPrototype:
        """Build and return TDEventVariableDataPrototype object.

        Returns:
            TDEventVariableDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
