"""DltArgument AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 983)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 13)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class DltArgument(Identifiable):
    """AUTOSAR DltArgument."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dlt_arguments": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class="DltArgument",
        ),  # dltArguments
        "length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # length
        "network": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # network
        "optional": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # optional
        "predefined_text": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # predefinedText
        "variable_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # variableLength
    }

    def __init__(self) -> None:
        """Initialize DltArgument."""
        super().__init__()
        self.dlt_arguments: list[DltArgument] = []
        self.length: Optional[PositiveInteger] = None
        self.network: Optional[SwDataDefProps] = None
        self.optional: Optional[Boolean] = None
        self.predefined_text: Optional[Boolean] = None
        self.variable_length: Optional[Boolean] = None


class DltArgumentBuilder:
    """Builder for DltArgument."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltArgument = DltArgument()

    def build(self) -> DltArgument:
        """Build and return DltArgument object.

        Returns:
            DltArgument instance
        """
        # TODO: Add validation
        return self._obj
