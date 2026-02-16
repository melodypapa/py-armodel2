"""EcucContainerValue AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)


class EcucContainerValue(Identifiable):
    """AUTOSAR EcucContainerValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "definition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcucContainerDef,
        ),  # definition
        "parameter_values": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucParameterValue,
        ),  # parameterValues
        "reference_values": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (EcucAbstractReference),
        ),  # referenceValues
        "sub_containers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucContainerValue,
        ),  # subContainers
    }

    def __init__(self) -> None:
        """Initialize EcucContainerValue."""
        super().__init__()
        self.definition: Optional[EcucContainerDef] = None
        self.parameter_values: list[EcucParameterValue] = []
        self.reference_values: list[Any] = []
        self.sub_containers: list[EcucContainerValue] = []


class EcucContainerValueBuilder:
    """Builder for EcucContainerValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucContainerValue = EcucContainerValue()

    def build(self) -> EcucContainerValue:
        """Build and return EcucContainerValue object.

        Returns:
            EcucContainerValue instance
        """
        # TODO: Add validation
        return self._obj
