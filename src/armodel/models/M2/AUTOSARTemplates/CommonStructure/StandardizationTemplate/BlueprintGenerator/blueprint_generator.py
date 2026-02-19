"""BlueprintGenerator AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 424)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintGenerator.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class BlueprintGenerator(ARObject):
    """AUTOSAR BlueprintGenerator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    expression: Optional[VerbatimString]
    introduction: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize BlueprintGenerator."""
        super().__init__()
        self.expression: Optional[VerbatimString] = None
        self.introduction: Optional[DocumentationBlock] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintGenerator":
        """Deserialize XML element to BlueprintGenerator object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintGenerator object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse expression
        child = ARObject._find_child_element(element, "EXPRESSION")
        if child is not None:
            expression_value = child.text
            obj.expression = expression_value

        # Parse introduction
        child = ARObject._find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        return obj



class BlueprintGeneratorBuilder:
    """Builder for BlueprintGenerator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintGenerator = BlueprintGenerator()

    def build(self) -> BlueprintGenerator:
        """Build and return BlueprintGenerator object.

        Returns:
            BlueprintGenerator instance
        """
        # TODO: Add validation
        return self._obj
