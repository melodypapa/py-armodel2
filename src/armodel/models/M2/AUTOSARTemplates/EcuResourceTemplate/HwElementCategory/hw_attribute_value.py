"""HwAttributeValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 16)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate_HwElementCategory.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_def import (
    HwAttributeDef,
)


class HwAttributeValue(ARObject):
    """AUTOSAR HwAttributeValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    annotation: Optional[Annotation]
    hw_attribute_def: Optional[HwAttributeDef]
    v: Optional[Numerical]
    vt: Optional[VerbatimString]
    def __init__(self) -> None:
        """Initialize HwAttributeValue."""
        super().__init__()
        self.annotation: Optional[Annotation] = None
        self.hw_attribute_def: Optional[HwAttributeDef] = None
        self.v: Optional[Numerical] = None
        self.vt: Optional[VerbatimString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwAttributeValue":
        """Deserialize XML element to HwAttributeValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwAttributeValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse annotation
        child = ARObject._find_child_element(element, "ANNOTATION")
        if child is not None:
            annotation_value = ARObject._deserialize_by_tag(child, "Annotation")
            obj.annotation = annotation_value

        # Parse hw_attribute_def
        child = ARObject._find_child_element(element, "HW-ATTRIBUTE-DEF")
        if child is not None:
            hw_attribute_def_value = ARObject._deserialize_by_tag(child, "HwAttributeDef")
            obj.hw_attribute_def = hw_attribute_def_value

        # Parse v
        child = ARObject._find_child_element(element, "V")
        if child is not None:
            v_value = child.text
            obj.v = v_value

        # Parse vt
        child = ARObject._find_child_element(element, "VT")
        if child is not None:
            vt_value = ARObject._deserialize_by_tag(child, "VerbatimString")
            obj.vt = vt_value

        return obj



class HwAttributeValueBuilder:
    """Builder for HwAttributeValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwAttributeValue = HwAttributeValue()

    def build(self) -> HwAttributeValue:
        """Build and return HwAttributeValue object.

        Returns:
            HwAttributeValue instance
        """
        # TODO: Add validation
        return self._obj
