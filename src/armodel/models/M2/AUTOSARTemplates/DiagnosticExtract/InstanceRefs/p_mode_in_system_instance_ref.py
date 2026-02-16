"""PModeInSystemInstanceRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class PModeInSystemInstanceRef(ARObject):
    """AUTOSAR PModeInSystemInstanceRef."""

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
        "context_mode_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # contextModeGroup
        "context_p_port_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractProvidedPortPrototype,
        ),  # contextPPortPrototype
        "target_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclaration,
        ),  # targetMode
    }

    def __init__(self) -> None:
        """Initialize PModeInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.context_mode_group: Optional[ModeDeclarationGroup] = None
        self.context_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None
        self.target_mode: Optional[ModeDeclaration] = None


class PModeInSystemInstanceRefBuilder:
    """Builder for PModeInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PModeInSystemInstanceRef = PModeInSystemInstanceRef()

    def build(self) -> PModeInSystemInstanceRef:
        """Build and return PModeInSystemInstanceRef object.

        Returns:
            PModeInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
