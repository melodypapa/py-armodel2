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
