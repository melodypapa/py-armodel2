"""CanTpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 611)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
    CanTpAddress,
)


class CanTpNode(Identifiable):
    """AUTOSAR CanTpNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "connector": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (Communication),
        ),  # connector
        "max_fc_wait": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxFcWait
        "st_min": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # stMin
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
        "tp_address": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CanTpAddress,
        ),  # tpAddress
    }

    def __init__(self) -> None:
        """Initialize CanTpNode."""
        super().__init__()
        self.connector: Optional[Any] = None
        self.max_fc_wait: Optional[Integer] = None
        self.st_min: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.tp_address: Optional[CanTpAddress] = None


class CanTpNodeBuilder:
    """Builder for CanTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpNode = CanTpNode()

    def build(self) -> CanTpNode:
        """Build and return CanTpNode object.

        Returns:
            CanTpNode instance
        """
        # TODO: Add validation
        return self._obj
