"""DiagnosticJ1939SwMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)


class DiagnosticJ1939SwMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticJ1939SwMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "node": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticJ1939Node,
        ),  # node
        "sw_component_prototype_composition_instance_ref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwComponentPrototype,
        ),  # swComponentPrototypeCompositionInstanceRef
    }

    def __init__(self) -> None:
        """Initialize DiagnosticJ1939SwMapping."""
        super().__init__()
        self.node: Optional[DiagnosticJ1939Node] = None
        self.sw_component_prototype_composition_instance_ref: Optional[SwComponentPrototype] = None


class DiagnosticJ1939SwMappingBuilder:
    """Builder for DiagnosticJ1939SwMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939SwMapping = DiagnosticJ1939SwMapping()

    def build(self) -> DiagnosticJ1939SwMapping:
        """Build and return DiagnosticJ1939SwMapping object.

        Returns:
            DiagnosticJ1939SwMapping instance
        """
        # TODO: Add validation
        return self._obj
