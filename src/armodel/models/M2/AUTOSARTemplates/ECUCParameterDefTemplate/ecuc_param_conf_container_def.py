"""EcucParamConfContainerDef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)


class EcucParamConfContainerDef(EcucContainerDef):
    """AUTOSAR EcucParamConfContainerDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "parameters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucParameterDef,
        ),  # parameters
        "references": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (EcucAbstractReference),
        ),  # references
        "sub_containers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucContainerDef,
        ),  # subContainers
    }

    def __init__(self) -> None:
        """Initialize EcucParamConfContainerDef."""
        super().__init__()
        self.parameters: list[EcucParameterDef] = []
        self.references: list[Any] = []
        self.sub_containers: list[EcucContainerDef] = []


class EcucParamConfContainerDefBuilder:
    """Builder for EcucParamConfContainerDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucParamConfContainerDef = EcucParamConfContainerDef()

    def build(self) -> EcucParamConfContainerDef:
        """Build and return EcucParamConfContainerDef object.

        Returns:
            EcucParamConfContainerDef instance
        """
        # TODO: Add validation
        return self._obj
