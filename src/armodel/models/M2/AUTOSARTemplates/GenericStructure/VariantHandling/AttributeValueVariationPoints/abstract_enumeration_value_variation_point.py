"""AbstractEnumerationValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 421)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Ref,
)
from abc import ABC, abstractmethod


class AbstractEnumerationValueVariationPoint(ARObject, ABC):
    """AUTOSAR AbstractEnumerationValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    base: Optional[Identifier]
    enum_table_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize AbstractEnumerationValueVariationPoint."""
        super().__init__()
        self.base: Optional[Identifier] = None
        self.enum_table_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractEnumerationValueVariationPoint":
        """Deserialize XML element to AbstractEnumerationValueVariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractEnumerationValueVariationPoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.base = base_value

        # Parse enum_table_ref
        child = ARObject._find_child_element(element, "ENUM-TABLE")
        if child is not None:
            enum_table_ref_value = ARObject._deserialize_by_tag(child, "Ref")
            obj.enum_table_ref = enum_table_ref_value

        return obj



class AbstractEnumerationValueVariationPointBuilder:
    """Builder for AbstractEnumerationValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractEnumerationValueVariationPoint = AbstractEnumerationValueVariationPoint()

    def build(self) -> AbstractEnumerationValueVariationPoint:
        """Build and return AbstractEnumerationValueVariationPoint object.

        Returns:
            AbstractEnumerationValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
