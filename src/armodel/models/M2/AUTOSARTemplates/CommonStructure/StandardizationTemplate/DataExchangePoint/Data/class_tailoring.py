"""ClassTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_content_conditional import (
    ClassContentConditional,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.variation_restriction_with_severity import (
    VariationRestrictionWithSeverity,
)
from abc import ABC, abstractmethod


class ClassTailoring(ARObject, ABC):
    """AUTOSAR ClassTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    class_contents: list[ClassContentConditional]
    multiplicity: Optional[Any]
    variation: Optional[VariationRestrictionWithSeverity]
    def __init__(self) -> None:
        """Initialize ClassTailoring."""
        super().__init__()
        self.class_contents: list[ClassContentConditional] = []
        self.multiplicity: Optional[Any] = None
        self.variation: Optional[VariationRestrictionWithSeverity] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClassTailoring":
        """Deserialize XML element to ClassTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClassTailoring object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse class_contents (list)
        obj.class_contents = []
        for child in ARObject._find_all_child_elements(element, "CLASS-CONTENTS"):
            class_contents_value = ARObject._deserialize_by_tag(child, "ClassContentConditional")
            obj.class_contents.append(class_contents_value)

        # Parse multiplicity
        child = ARObject._find_child_element(element, "MULTIPLICITY")
        if child is not None:
            multiplicity_value = child.text
            obj.multiplicity = multiplicity_value

        # Parse variation
        child = ARObject._find_child_element(element, "VARIATION")
        if child is not None:
            variation_value = ARObject._deserialize_by_tag(child, "VariationRestrictionWithSeverity")
            obj.variation = variation_value

        return obj



class ClassTailoringBuilder:
    """Builder for ClassTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClassTailoring = ClassTailoring()

    def build(self) -> ClassTailoring:
        """Build and return ClassTailoring object.

        Returns:
            ClassTailoring instance
        """
        # TODO: Add validation
        return self._obj
