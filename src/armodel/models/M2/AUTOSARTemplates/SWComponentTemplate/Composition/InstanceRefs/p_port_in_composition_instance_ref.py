"""PPortInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 951)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)


class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """AUTOSAR PPortInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "context": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # context
        "target_p_port_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractProvidedPortPrototype,
        ),  # targetPPortPrototype
    }

    def __init__(self) -> None:
        """Initialize PPortInCompositionInstanceRef."""
        super().__init__()
        self.context: Optional[Any] = None
        self.target_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None


class PPortInCompositionInstanceRefBuilder:
    """Builder for PPortInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PPortInCompositionInstanceRef = PPortInCompositionInstanceRef()

    def build(self) -> PPortInCompositionInstanceRef:
        """Build and return PPortInCompositionInstanceRef object.

        Returns:
            PPortInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
