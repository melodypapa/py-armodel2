"""EcucChoiceContainerDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 41)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_param_conf_container_def import (
    EcucParamConfContainerDef,
)


class EcucChoiceContainerDef(EcucContainerDef):
    """AUTOSAR EcucChoiceContainerDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    choices: list[EcucParamConfContainerDef]
    def __init__(self) -> None:
        """Initialize EcucChoiceContainerDef."""
        super().__init__()
        self.choices: list[EcucParamConfContainerDef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucChoiceContainerDef":
        """Deserialize XML element to EcucChoiceContainerDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucChoiceContainerDef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse choices (list)
        obj.choices = []
        for child in ARObject._find_all_child_elements(element, "CHOICES"):
            choices_value = ARObject._deserialize_by_tag(child, "EcucParamConfContainerDef")
            obj.choices.append(choices_value)

        return obj



class EcucChoiceContainerDefBuilder:
    """Builder for EcucChoiceContainerDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucChoiceContainerDef = EcucChoiceContainerDef()

    def build(self) -> EcucChoiceContainerDef:
        """Build and return EcucChoiceContainerDef object.

        Returns:
            EcucChoiceContainerDef instance
        """
        # TODO: Add validation
        return self._obj
