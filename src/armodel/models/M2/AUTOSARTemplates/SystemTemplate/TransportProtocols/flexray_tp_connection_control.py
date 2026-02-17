"""FlexrayTpConnectionControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 593)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)


class FlexrayTpConnectionControl(Identifiable):
    """AUTOSAR FlexrayTpConnectionControl."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ack_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FrArTpAckType,
        ),  # ackType
        "max_fc_wait": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxFcWait
        "max_number_of": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxNumberOf
        "max_retries": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxRetries
        "separation_cycle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # separationCycle
        "time_br": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeBr
        "time_buffer": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeBuffer
        "time_cs": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeCs
        "timeout_ar": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeoutAr
        "timeout_as": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeoutAs
        "timeout_bs": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeoutBs
        "timeout_cr": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeoutCr
    }

    def __init__(self) -> None:
        """Initialize FlexrayTpConnectionControl."""
        super().__init__()
        self.ack_type: Optional[FrArTpAckType] = None
        self.max_fc_wait: Optional[Integer] = None
        self.max_number_of: Optional[Integer] = None
        self.max_retries: Optional[Integer] = None
        self.separation_cycle: Optional[Integer] = None
        self.time_br: Optional[TimeValue] = None
        self.time_buffer: Optional[TimeValue] = None
        self.time_cs: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_bs: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None


class FlexrayTpConnectionControlBuilder:
    """Builder for FlexrayTpConnectionControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpConnectionControl = FlexrayTpConnectionControl()

    def build(self) -> FlexrayTpConnectionControl:
        """Build and return FlexrayTpConnectionControl object.

        Returns:
            FlexrayTpConnectionControl instance
        """
        # TODO: Add validation
        return self._obj
