"""GeneralAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 162)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_GeneralAnnotation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from abc import ABC, abstractmethod


class GeneralAnnotation(ARObject, ABC):
    """AUTOSAR GeneralAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    annotation: String
    annotation_text: DocumentationBlock
    label: Optional[MultilanguageLongName]
    def __init__(self) -> None:
        """Initialize GeneralAnnotation."""
        super().__init__()
        self.annotation: String = None
        self.annotation_text: DocumentationBlock = None
        self.label: Optional[MultilanguageLongName] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "GeneralAnnotation":
        """Deserialize XML element to GeneralAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GeneralAnnotation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse annotation
        child = ARObject._find_child_element(element, "ANNOTATION")
        if child is not None:
            annotation_value = child.text
            obj.annotation = annotation_value

        # Parse annotation_text
        child = ARObject._find_child_element(element, "ANNOTATION-TEXT")
        if child is not None:
            annotation_text_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.annotation_text = annotation_text_value

        # Parse label
        child = ARObject._find_child_element(element, "LABEL")
        if child is not None:
            label_value = ARObject._deserialize_by_tag(child, "MultilanguageLongName")
            obj.label = label_value

        return obj



class GeneralAnnotationBuilder:
    """Builder for GeneralAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GeneralAnnotation = GeneralAnnotation()

    def build(self) -> GeneralAnnotation:
        """Build and return GeneralAnnotation object.

        Returns:
            GeneralAnnotation instance
        """
        # TODO: Add validation
        return self._obj
