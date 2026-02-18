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
