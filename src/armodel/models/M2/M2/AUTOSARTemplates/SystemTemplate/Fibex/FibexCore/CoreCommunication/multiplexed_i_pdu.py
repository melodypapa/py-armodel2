"""MultiplexedIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 408)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.dynamic_part import (
    DynamicPart,
)


class MultiplexedIPdu(IPdu):
    """AUTOSAR MultiplexedIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dynamic_part": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DynamicPart,
        ),  # dynamicPart
        "selector_field": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # selectorField
        "unused_bit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # unusedBit
    }

    def __init__(self) -> None:
        """Initialize MultiplexedIPdu."""
        super().__init__()
        self.dynamic_part: Optional[DynamicPart] = None
        self.selector_field: Optional[Integer] = None
        self.unused_bit: Optional[Integer] = None


class MultiplexedIPduBuilder:
    """Builder for MultiplexedIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiplexedIPdu = MultiplexedIPdu()

    def build(self) -> MultiplexedIPdu:
        """Build and return MultiplexedIPdu object.

        Returns:
            MultiplexedIPdu instance
        """
        # TODO: Add validation
        return self._obj
