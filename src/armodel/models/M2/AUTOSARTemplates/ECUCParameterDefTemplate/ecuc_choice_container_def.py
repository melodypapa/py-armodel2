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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucChoiceContainerDef, cls).deserialize(element)

        # Parse choices (list from container "CHOICES")
        obj.choices = []
        container = ARObject._find_child_element(element, "CHOICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.choices.append(child_value)

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
