"""AttributeValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 617)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 209)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 41)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PrimitiveIdentifier,
    String,
)
from abc import ABC, abstractmethod


class AttributeValueVariationPoint(ARObject, ABC):
    """AUTOSAR AttributeValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    binding_time_enum: Optional[BindingTimeEnum]
    blueprint_value: Optional[String]
    sd: Optional[String]
    short_label: Optional[PrimitiveIdentifier]
    def __init__(self) -> None:
        """Initialize AttributeValueVariationPoint."""
        super().__init__()
        self.binding_time_enum: Optional[BindingTimeEnum] = None
        self.blueprint_value: Optional[String] = None
        self.sd: Optional[String] = None
        self.short_label: Optional[PrimitiveIdentifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AttributeValueVariationPoint":
        """Deserialize XML element to AttributeValueVariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AttributeValueVariationPoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse binding_time_enum
        child = ARObject._find_child_element(element, "BINDING-TIME-ENUM")
        if child is not None:
            binding_time_enum_value = child.text
            obj.binding_time_enum = binding_time_enum_value

        # Parse blueprint_value
        child = ARObject._find_child_element(element, "BLUEPRINT-VALUE")
        if child is not None:
            blueprint_value_value = child.text
            obj.blueprint_value = blueprint_value_value

        # Parse sd
        child = ARObject._find_child_element(element, "SD")
        if child is not None:
            sd_value = child.text
            obj.sd = sd_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        return obj



class AttributeValueVariationPointBuilder:
    """Builder for AttributeValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AttributeValueVariationPoint = AttributeValueVariationPoint()

    def build(self) -> AttributeValueVariationPoint:
        """Build and return AttributeValueVariationPoint object.

        Returns:
            AttributeValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
