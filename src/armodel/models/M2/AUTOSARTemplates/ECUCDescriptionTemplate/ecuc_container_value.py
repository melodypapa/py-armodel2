"""EcucContainerValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 119)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2021)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 439)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 185)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)


class EcucContainerValue(Identifiable):
    """AUTOSAR EcucContainerValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    definition: Optional[EcucContainerDef]
    parameter_values: list[EcucParameterValue]
    reference_value_refs: list[ARRef]
    sub_containers: list[EcucContainerValue]
    def __init__(self) -> None:
        """Initialize EcucContainerValue."""
        super().__init__()
        self.definition: Optional[EcucContainerDef] = None
        self.parameter_values: list[EcucParameterValue] = []
        self.reference_value_refs: list[ARRef] = []
        self.sub_containers: list[EcucContainerValue] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucContainerValue":
        """Deserialize XML element to EcucContainerValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucContainerValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse definition
        child = ARObject._find_child_element(element, "DEFINITION")
        if child is not None:
            definition_value = ARObject._deserialize_by_tag(child, "EcucContainerDef")
            obj.definition = definition_value

        # Parse parameter_values (list)
        obj.parameter_values = []
        for child in ARObject._find_all_child_elements(element, "PARAMETER-VALUES"):
            parameter_values_value = ARObject._deserialize_by_tag(child, "EcucParameterValue")
            obj.parameter_values.append(parameter_values_value)

        # Parse reference_value_refs (list)
        obj.reference_value_refs = []
        for child in ARObject._find_all_child_elements(element, "REFERENCE-VALUES"):
            reference_value_refs_value = child.text
            obj.reference_value_refs.append(reference_value_refs_value)

        # Parse sub_containers (list)
        obj.sub_containers = []
        for child in ARObject._find_all_child_elements(element, "SUB-CONTAINERS"):
            sub_containers_value = ARObject._deserialize_by_tag(child, "EcucContainerValue")
            obj.sub_containers.append(sub_containers_value)

        return obj



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
