"""ModeInSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 38)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class ModeInSwcInstanceRef(ARObject):
    """AUTOSAR ModeInSwcInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwComponentType,
        ),  # base
        "contexts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # contexts
        "context_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # contextMode
        "context_port": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PortPrototype,
        ),  # contextPort
        "target_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclaration,
        ),  # targetMode
    }

    def __init__(self) -> None:
        """Initialize ModeInSwcInstanceRef."""
        super().__init__()
        self.base: Optional[SwComponentType] = None
        self.contexts: list[Any] = []
        self.context_mode: Optional[ModeDeclarationGroup] = None
        self.context_port: Optional[PortPrototype] = None
        self.target_mode: Optional[ModeDeclaration] = None


class ModeInSwcInstanceRefBuilder:
    """Builder for ModeInSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInSwcInstanceRef = ModeInSwcInstanceRef()

    def build(self) -> ModeInSwcInstanceRef:
        """Build and return ModeInSwcInstanceRef object.

        Returns:
            ModeInSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
