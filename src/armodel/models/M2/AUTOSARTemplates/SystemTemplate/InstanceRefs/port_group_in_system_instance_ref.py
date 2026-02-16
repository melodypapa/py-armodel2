"""PortGroupInSystemInstanceRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class PortGroupInSystemInstanceRef(ARObject):
    """AUTOSAR PortGroupInSystemInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=System,
        ),  # base
        "context": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RootSwCompositionPrototype,
        ),  # context
        "target": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=PortGroup,
        ),  # target
    }

    def __init__(self) -> None:
        """Initialize PortGroupInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.target: PortGroup = None


class PortGroupInSystemInstanceRefBuilder:
    """Builder for PortGroupInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortGroupInSystemInstanceRef = PortGroupInSystemInstanceRef()

    def build(self) -> PortGroupInSystemInstanceRef:
        """Build and return PortGroupInSystemInstanceRef object.

        Returns:
            PortGroupInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
