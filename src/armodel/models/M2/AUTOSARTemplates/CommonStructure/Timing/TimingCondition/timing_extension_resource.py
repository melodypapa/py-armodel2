"""TimingExtensionResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TimingExtensionResource(Identifiable):
    """AUTOSAR TimingExtensionResource."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "timing_arguments": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AutosarOperationArgumentInstance,
        ),  # timingArguments
        "timing_modes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TimingModeInstance,
        ),  # timingModes
        "timing_variables": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (AutosarVariable),
        ),  # timingVariables
    }

    def __init__(self) -> None:
        """Initialize TimingExtensionResource."""
        super().__init__()
        self.timing_arguments: list[AutosarOperationArgumentInstance] = []
        self.timing_modes: list[TimingModeInstance] = []
        self.timing_variables: list[Any] = []


class TimingExtensionResourceBuilder:
    """Builder for TimingExtensionResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingExtensionResource = TimingExtensionResource()

    def build(self) -> TimingExtensionResource:
        """Build and return TimingExtensionResource object.

        Returns:
            TimingExtensionResource instance
        """
        # TODO: Add validation
        return self._obj
