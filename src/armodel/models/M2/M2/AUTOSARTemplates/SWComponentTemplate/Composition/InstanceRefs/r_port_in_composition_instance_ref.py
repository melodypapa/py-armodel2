"""RPortInCompositionInstanceRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)


class RPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """AUTOSAR RPortInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "context": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SwComponent),
        ),  # context
        "target_r_port_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractRequiredPortPrototype,
        ),  # targetRPortPrototype
    }

    def __init__(self) -> None:
        """Initialize RPortInCompositionInstanceRef."""
        super().__init__()
        self.context: Optional[Any] = None
        self.target_r_port_prototype: Optional[AbstractRequiredPortPrototype] = None


class RPortInCompositionInstanceRefBuilder:
    """Builder for RPortInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RPortInCompositionInstanceRef = RPortInCompositionInstanceRef()

    def build(self) -> RPortInCompositionInstanceRef:
        """Build and return RPortInCompositionInstanceRef object.

        Returns:
            RPortInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
