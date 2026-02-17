"""SystemSignalGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 324)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SystemSignalGroup(ARElement):
    """AUTOSAR SystemSignalGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "system_signals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SystemSignal,
        ),  # systemSignals
        "transforming": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SystemSignal,
        ),  # transforming
    }

    def __init__(self) -> None:
        """Initialize SystemSignalGroup."""
        super().__init__()
        self.system_signals: list[SystemSignal] = []
        self.transforming: Optional[SystemSignal] = None


class SystemSignalGroupBuilder:
    """Builder for SystemSignalGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemSignalGroup = SystemSignalGroup()

    def build(self) -> SystemSignalGroup:
        """Build and return SystemSignalGroup object.

        Returns:
            SystemSignalGroup instance
        """
        # TODO: Add validation
        return self._obj
