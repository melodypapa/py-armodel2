"""EcucAbstractReferenceValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_indexable_value import (
    EcucIndexableValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from abc import ABC, abstractmethod


class EcucAbstractReferenceValue(EcucIndexableValue, ABC):
    """AUTOSAR EcucAbstractReferenceValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    annotations: list[Annotation]
    definition_ref: Optional[ARRef]
    is_auto_value: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucAbstractReferenceValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.definition_ref: Optional[ARRef] = None
        self.is_auto_value: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractReferenceValue":
        """Deserialize XML element to EcucAbstractReferenceValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAbstractReferenceValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse annotations (list)
        obj.annotations = []
        for child in ARObject._find_all_child_elements(element, "ANNOTATIONS"):
            annotations_value = ARObject._deserialize_by_tag(child, "Annotation")
            obj.annotations.append(annotations_value)

        # Parse definition_ref
        child = ARObject._find_child_element(element, "DEFINITION")
        if child is not None:
            definition_ref_value = child.text
            obj.definition_ref = definition_ref_value

        # Parse is_auto_value
        child = ARObject._find_child_element(element, "IS-AUTO-VALUE")
        if child is not None:
            is_auto_value_value = child.text
            obj.is_auto_value = is_auto_value_value

        return obj



class EcucAbstractReferenceValueBuilder:
    """Builder for EcucAbstractReferenceValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractReferenceValue = EcucAbstractReferenceValue()

    def build(self) -> EcucAbstractReferenceValue:
        """Build and return EcucAbstractReferenceValue object.

        Returns:
            EcucAbstractReferenceValue instance
        """
        # TODO: Add validation
        return self._obj
