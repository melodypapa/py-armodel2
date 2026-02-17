"""ISignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 846)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)


class ISignalMapping(ARObject):
    """AUTOSAR ISignalMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "introduction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # introduction
        "source_signal": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ISignalTriggering,
        ),  # sourceSignal
        "target_signal": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ISignalTriggering,
        ),  # targetSignal
    }

    def __init__(self) -> None:
        """Initialize ISignalMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
        self.source_signal: Optional[ISignalTriggering] = None
        self.target_signal: Optional[ISignalTriggering] = None


class ISignalMappingBuilder:
    """Builder for ISignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalMapping = ISignalMapping()

    def build(self) -> ISignalMapping:
        """Build and return ISignalMapping object.

        Returns:
            ISignalMapping instance
        """
        # TODO: Add validation
        return self._obj
