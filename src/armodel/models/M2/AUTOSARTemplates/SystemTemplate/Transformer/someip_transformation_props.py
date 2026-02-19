"""SOMEIPTransformationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 783)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SOMEIPTransformationProps(TransformationProps):
    """AUTOSAR SOMEIPTransformationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alignment: Optional[PositiveInteger]
    size_of_array: Optional[PositiveInteger]
    size_of_string: Optional[PositiveInteger]
    size_of_struct: Optional[PositiveInteger]
    size_of_union: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SOMEIPTransformationProps."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.size_of_array: Optional[PositiveInteger] = None
        self.size_of_string: Optional[PositiveInteger] = None
        self.size_of_struct: Optional[PositiveInteger] = None
        self.size_of_union: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SOMEIPTransformationProps":
        """Deserialize XML element to SOMEIPTransformationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SOMEIPTransformationProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse alignment
        child = ARObject._find_child_element(element, "ALIGNMENT")
        if child is not None:
            alignment_value = child.text
            obj.alignment = alignment_value

        # Parse size_of_array
        child = ARObject._find_child_element(element, "SIZE-OF-ARRAY")
        if child is not None:
            size_of_array_value = child.text
            obj.size_of_array = size_of_array_value

        # Parse size_of_string
        child = ARObject._find_child_element(element, "SIZE-OF-STRING")
        if child is not None:
            size_of_string_value = child.text
            obj.size_of_string = size_of_string_value

        # Parse size_of_struct
        child = ARObject._find_child_element(element, "SIZE-OF-STRUCT")
        if child is not None:
            size_of_struct_value = child.text
            obj.size_of_struct = size_of_struct_value

        # Parse size_of_union
        child = ARObject._find_child_element(element, "SIZE-OF-UNION")
        if child is not None:
            size_of_union_value = child.text
            obj.size_of_union = size_of_union_value

        return obj



class SOMEIPTransformationPropsBuilder:
    """Builder for SOMEIPTransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SOMEIPTransformationProps = SOMEIPTransformationProps()

    def build(self) -> SOMEIPTransformationProps:
        """Build and return SOMEIPTransformationProps object.

        Returns:
            SOMEIPTransformationProps instance
        """
        # TODO: Add validation
        return self._obj
