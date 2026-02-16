"""BuildActionIoElement AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class BuildActionIoElement(ARObject):
    """AUTOSAR BuildActionIoElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "category": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # category
        "ecuc_definition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcucDefinitionElement,
        ),  # ecucDefinition
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # role
        "sdgs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Sdg,
        ),  # sdgs
    }

    def __init__(self) -> None:
        """Initialize BuildActionIoElement."""
        super().__init__()
        self.category: NameToken = None
        self.ecuc_definition: Optional[EcucDefinitionElement] = None
        self.role: Optional[Identifier] = None
        self.sdgs: list[Sdg] = []


class BuildActionIoElementBuilder:
    """Builder for BuildActionIoElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionIoElement = BuildActionIoElement()

    def build(self) -> BuildActionIoElement:
        """Build and return BuildActionIoElement object.

        Returns:
            BuildActionIoElement instance
        """
        # TODO: Add validation
        return self._obj
