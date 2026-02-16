"""InnerPortGroupInCompositionInstanceRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)


class InnerPortGroupInCompositionInstanceRef(ARObject):
    """AUTOSAR InnerPortGroupInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompositionSwComponentType,
        ),  # base
        "contexts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SwComponent),
        ),  # contexts
        "target": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PortGroup,
        ),  # target
    }

    def __init__(self) -> None:
        """Initialize InnerPortGroupInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.contexts: list[Any] = []
        self.target: Optional[PortGroup] = None


class InnerPortGroupInCompositionInstanceRefBuilder:
    """Builder for InnerPortGroupInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InnerPortGroupInCompositionInstanceRef = InnerPortGroupInCompositionInstanceRef()

    def build(self) -> InnerPortGroupInCompositionInstanceRef:
        """Build and return InnerPortGroupInCompositionInstanceRef object.

        Returns:
            InnerPortGroupInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
