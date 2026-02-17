"""PortPrototypeBlueprintInitValue AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 60)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintDedicated_Port.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class PortPrototypeBlueprintInitValue(ARObject):
    """AUTOSAR PortPrototypeBlueprintInitValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=AutosarDataPrototype,
        ),  # dataPrototype
        "value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=ValueSpecification,
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize PortPrototypeBlueprintInitValue."""
        super().__init__()
        self.data_prototype: AutosarDataPrototype = None
        self.value: ValueSpecification = None


class PortPrototypeBlueprintInitValueBuilder:
    """Builder for PortPrototypeBlueprintInitValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortPrototypeBlueprintInitValue = PortPrototypeBlueprintInitValue()

    def build(self) -> PortPrototypeBlueprintInitValue:
        """Build and return PortPrototypeBlueprintInitValue object.

        Returns:
            PortPrototypeBlueprintInitValue instance
        """
        # TODO: Add validation
        return self._obj
