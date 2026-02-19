"""SOMEIPTransformationDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 777)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SOMEIPTransformationDescription(TransformationDescription):
    """AUTOSAR SOMEIPTransformationDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alignment: Optional[PositiveInteger]
    byte_order: Optional[ByteOrderEnum]
    interface_version: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SOMEIPTransformationDescription."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.byte_order: Optional[ByteOrderEnum] = None
        self.interface_version: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SOMEIPTransformationDescription":
        """Deserialize XML element to SOMEIPTransformationDescription object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SOMEIPTransformationDescription object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse alignment
        child = ARObject._find_child_element(element, "ALIGNMENT")
        if child is not None:
            alignment_value = child.text
            obj.alignment = alignment_value

        # Parse byte_order
        child = ARObject._find_child_element(element, "BYTE-ORDER")
        if child is not None:
            byte_order_value = child.text
            obj.byte_order = byte_order_value

        # Parse interface_version
        child = ARObject._find_child_element(element, "INTERFACE-VERSION")
        if child is not None:
            interface_version_value = child.text
            obj.interface_version = interface_version_value

        return obj



class SOMEIPTransformationDescriptionBuilder:
    """Builder for SOMEIPTransformationDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SOMEIPTransformationDescription = SOMEIPTransformationDescription()

    def build(self) -> SOMEIPTransformationDescription:
        """Build and return SOMEIPTransformationDescription object.

        Returns:
            SOMEIPTransformationDescription instance
        """
        # TODO: Add validation
        return self._obj
