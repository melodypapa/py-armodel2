"""EcucChoiceReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 74)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
    EcucAbstractInternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)


class EcucChoiceReferenceDef(EcucAbstractInternalReferenceDef):
    """AUTOSAR EcucChoiceReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destinations: list[EcucContainerDef]
    def __init__(self) -> None:
        """Initialize EcucChoiceReferenceDef."""
        super().__init__()
        self.destinations: list[EcucContainerDef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucChoiceReferenceDef":
        """Deserialize XML element to EcucChoiceReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucChoiceReferenceDef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse destinations (list)
        obj.destinations = []
        for child in ARObject._find_all_child_elements(element, "DESTINATIONS"):
            destinations_value = ARObject._deserialize_by_tag(child, "EcucContainerDef")
            obj.destinations.append(destinations_value)

        return obj



class EcucChoiceReferenceDefBuilder:
    """Builder for EcucChoiceReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucChoiceReferenceDef = EcucChoiceReferenceDef()

    def build(self) -> EcucChoiceReferenceDef:
        """Build and return EcucChoiceReferenceDef object.

        Returns:
            EcucChoiceReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
