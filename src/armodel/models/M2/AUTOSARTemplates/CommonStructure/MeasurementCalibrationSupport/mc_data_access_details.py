"""McDataAccessDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)


class McDataAccessDetails(ARObject):
    """AUTOSAR McDataAccessDetails."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "rte_event_refs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RTEEvent,
        ),  # rteEventRefs
        "variable_accesses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableAccess,
        ),  # variableAccesses
    }

    def __init__(self) -> None:
        """Initialize McDataAccessDetails."""
        super().__init__()
        self.rte_event_refs: list[RTEEvent] = []
        self.variable_accesses: list[VariableAccess] = []


class McDataAccessDetailsBuilder:
    """Builder for McDataAccessDetails."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McDataAccessDetails = McDataAccessDetails()

    def build(self) -> McDataAccessDetails:
        """Build and return McDataAccessDetails object.

        Returns:
            McDataAccessDetails instance
        """
        # TODO: Add validation
        return self._obj
