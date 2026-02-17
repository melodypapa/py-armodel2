"""PortDefinedArgumentValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 593)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class PortDefinedArgumentValue(ARObject):
    """AUTOSAR PortDefinedArgumentValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # value
        "value_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # valueType
    }

    def __init__(self) -> None:
        """Initialize PortDefinedArgumentValue."""
        super().__init__()
        self.value: Optional[ValueSpecification] = None
        self.value_type: Optional[Any] = None


class PortDefinedArgumentValueBuilder:
    """Builder for PortDefinedArgumentValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortDefinedArgumentValue = PortDefinedArgumentValue()

    def build(self) -> PortDefinedArgumentValue:
        """Build and return PortDefinedArgumentValue object.

        Returns:
            PortDefinedArgumentValue instance
        """
        # TODO: Add validation
        return self._obj
